# Unicorn PS E:\Urban\rep\Urban-University-Homework\module_16_fastapi> python.exe -m uvicorn work_space:app
# Get - адрес в строке браузера ?переменная=значение
# Post - форма Оформить заказ в магазине
# Put - обновить данные
# Delete - удалить
# /docs - документация

from fastapi import FastAPI

app = FastAPI()


@app.get('/')  # slag
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
