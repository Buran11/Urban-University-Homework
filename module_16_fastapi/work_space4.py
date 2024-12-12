from fastapi import FastAPI, status, HTTPException, Body, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

message_db = []


class Message(BaseModel):
    id: int = None
    text: str


@app.get('/')
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('message.html', {'request': request, 'messages': message_db})


@app.get(path='/message/{message_id}')
async def get_message(request: Request, message_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse('message.html', {'request': request, 'message': message_db[message_id]})
    except KeyError:
        raise HTTPException(status_code=404, detail='Message not found')


@app.post('/', status_code=status.HTTP_201_CREATED)
async def create_message(request: Request, message: str = Form()) -> HTMLResponse:
    if message_db:
        message_id = max(message_db, key=lambda m: m.id).id + 1
    else:
        message_id = 0
    message_db.append(Message(id=message_id, text=message))
    return templates.TemplateResponse('message.html', {'request': request, 'message': message_db[message_id]})


@app.put('/message/{message_id}')
async def update_user(message_id: str, message: str = Body()) -> str:
    try:
        edit_message = message_db[message_id]
        edit_message.text = message
        return 'Message updated!'
    except KeyError:
        raise HTTPException(status_code=404, detail='Message not found')


@app.delete('/message/{message_id}')
async def delete_message(message_id: int) -> str:
    try:
        message_db.pop(message_id)
        return f'Message ID={message_id} deleted!'
    except KeyError:
        raise HTTPException(status_code=404, detail='Message not found')


@app.delete('/')
async def kill_message_all() -> str:
    message_db.clear()
    return f'All messages deleted!'
