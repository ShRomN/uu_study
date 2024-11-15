from fastapi import FastAPI, Path
from typing import Annotated
import uvicorn

app = FastAPI()


@app.get('/')
async def main_page() -> str:
    """
    Функция обработки запроса при обращении к главной странице.
    :return: строка с ответным сообщением.
    """
    return 'Главная страница'


@app.get('/user/admin')
async def admin_page() -> str:
    """
    Функция обработки запроса при обращении к странице администратора.
    :return: строка с ответным сообщением.
    """
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def user_id_page(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> str:
    """
    Функция обработки запроса при обращении к странице пользователя с конкретным id.
    :param user_id: идентификатор пользователя к станце которого идет запрос.
    :return: строка с ответным сообщением.
    """
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user/{username}/{age}')
async def user_info_page(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                         age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> str:
    """
    Функция обработки запроса при обращении к странице пользователя с передачей параметров.
    :param username: имя полбзователя;
    :param age: возраст пользователя.
    :return: строка с ответным сообщением.
    """
    return f"Информация о пользователе. Имя: '{username}', Возраст: {age}"



if __name__ == "__main__":
    uvicorn.run("module_16_2:app", host='127.0.0.1', port=8000, reload=True)
