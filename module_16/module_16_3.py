from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()

# Импровизированная база
users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_users() -> dict:
    """
    Функция обработки запроса при обращении к странице с пользователями.
    :return: словарь с информацией о пользователях в базе.
    """
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                         age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    """
    Функция обработки запроса добавления нового пользователя в базу.
    :param username: имя нового пользователя;
    :param age: возраст нового пользователя.
    :return: строка с ответным сообщением.
    """
    id = int(max(users)) + 1
    users[str(id)] = f'Имя: {username}, возраст: {age}'
    return f"User {id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)],
                       username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    """
    Функция обработки запроса обновления сведений о пользователе в базе.
    :param user_id: идентификатор пользователя данные о котором обновляются;
    :param username: имя пользователя;
    :param age: возраст пользователя.
    :return: строка с ответным сообщением.
    """
    if str(user_id) in users:
        users[str(user_id)] = f'Имя: {username}, возраст: {age}'
        return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    """
    Функция обработки запроса удаления пользователя из базы.
    :param user_id: идентификатор удаляемого пользователя.
    :return: строка с ответным сообщением.
    """
    if str(user_id) in users:
        del users[str(user_id)]
        return f'User {user_id} has been deleted'



if __name__ == "__main__":
    uvicorn.run("module_16_3:app", host='127.0.0.1', port=8000, reload=True)
