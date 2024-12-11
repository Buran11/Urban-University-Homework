from fastapi import FastAPI, status, HTTPException, Body
from pydantic import BaseModel
from typing import List

app = FastAPI()

message_db = []


class Message(BaseModel):
    id: int = None
    text: str


@app.get('/')
async def get_all_messages() -> List[Message]:
    return message_db


@app.get(path='/message/{message_id}')
async def get_message(message_id: int) -> Message:
    try:
        return message_db[message_id]
    except KeyError:
        raise HTTPException(status_code=404, detail='Message not found')


@app.post('/message')
async def create_message(message: Message) -> str:
    message.id = len(message_db)
    message_db.append(message)
    return 'Message created!'


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
