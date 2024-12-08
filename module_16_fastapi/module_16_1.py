# 2024/02/16 00:00|Домашнее задание по теме "Основы Fast Api и маршрутизация"
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_main_page() -> dict:
    return {'message': 'Главная страница'}


@app.get('/user/admin')
async def get_admin_page() -> dict:
    return {'message': 'Вы вошли как администратор'}


@app.get('/user/{user_id}')
async def get_user_id(user_id: int) -> dict:
    return {'message': f'Вы вошли как пользователь № {user_id}'}


@app.get('/user/')
async def get_user_info(username: str = 'Slava', age: int = '39') -> dict:
    return {'message': f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
