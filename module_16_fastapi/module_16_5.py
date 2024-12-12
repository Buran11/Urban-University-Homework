# 2024/02/23 00:00|Домашнее задание по теме "Шаблонизатор Jinja 2."
from fastapi import FastAPI, Path, HTTPException
from typing import Annotated

from pydantic import BaseModel

from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request, Form


app = FastAPI()
templates = Jinja2Templates(directory='templates')

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get('/')
async def get_main_page(request: Request) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'Users': users})


@app.get('/user/{user_id}')
async def get_users(request: Request, user_id: int) -> HTMLResponse:
    return templates.TemplateResponse('users.html', {'request': request, 'user': users[user_id - 1]})


@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='montes')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='25')]) -> User:
    if len(users) != 0:
        user_id = users[-1].id + 1
    else:
        user_id = 1
    users.append(User(id=user_id, username=username, age=age))
    return users[-1]


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='montes')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='25')]) -> User:
    for user in users:
        if user.id > len(users):
            raise HTTPException(
                status_code=404, detail='User was not found')
        if user.id != user_id:
            continue
        else:
            user.username = username
            user.age = age
            return user


@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> User:
    for user in users:
        if user.id > len(users):
            raise HTTPException(
                status_code=404, detail='User was not found')
        if user.id != user_id:
            continue
        else:
            users.remove(user)
            return user
