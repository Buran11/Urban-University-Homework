from fastapi import FastAPI

app = FastAPI()

message_db = {'0': 'First post in FastApi'}


@app.get('/')
async def get_all_messages() -> dict:
    return message_db


@app.get('/message/{message_id}')
async def get_message(message_id: int) -> dict:
    return message_db[message_id]


@app.post('/message')
async def create_message(message: str) -> str:
    current_index = str(int(max(message_db, key=int)) + 1)
    message_db[current_index] = message
    return 'Message created!'


@app.put('/message/{message_id}')
async def update_user(message_id: str, message: str) -> str:
    message_db[message_id] = message
    return f'Message updated!'


@app.delete('/message/{message_id}')
async def delete_message(message_id: int) -> str:
    message_db.pop(message_id)
    return f'Message with {message_id} was deleted!'


@app.delete('/')
async def delete_all_messages() -> str:
    message_db.clear()
    return f'All messages deleted!'
