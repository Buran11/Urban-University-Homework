# Unicorn PS E:\Urban\rep\Urban-University-Homework\module_16_fastapi> python.exe -m uvicorn work_space:app
# Get - адрес в строке браузера ?переменная=значение
# Post - форма Оформить заказ в магазине
# Put - обновить данные
# Delete - удалить
# /docs - документация

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')  # Swagger
async def welcome() -> dict:
    return {'message': 'Hello World'}


@app.get('/user/A/B')  # http://127.0.0.1:8000/user/A/B
async def news() -> dict:
    return {'message': 'Hello, tester!'}


@app.get('/id')  # http://127.0.0.1:8000/id?username=user&age=39
async def id_paginator(username: str, age: int) -> dict:
    return {'username': username, 'age': age}


@app.get('/id')  # http://127.0.0.1:8000/id значения по умолчанию
async def id_paginator(username: str = 'Slava', age: int = 39) -> dict:
    return {'username': username, 'age': age}


# http://127.0.0.1:8000/user/John/Doe
@app.get('/user/{first_name}/{last_name}')
async def news(first_name: str, last_name: str) -> dict:
    return {'message': f'Hello, {first_name} {last_name}'}


# Path - валидация
# @app.get('/user/{username}/{id}')
# async def news(username: str = Path(min_length=3, max_length=15, description='Enter your username', example='montes'),
#                id: int = Path(ge=0, le=100, description='Enter your id', example='75')) -> dict:
#     return {'message': f'Hello, {username}: {id}'}


# Pydentic - валидация
@app.get('/user/{username}/{id}')
async def news(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter your username', example='montes')], id: int) -> dict:
    return {'message': f'Hello, {username}: {id}'}
