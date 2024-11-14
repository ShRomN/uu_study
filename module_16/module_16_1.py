from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get('/')
async def main_page() -> str:
    """
    Функция обработки запроса при обращении к главной странице.
    :return: словарь с ответным сообщением.
    """
    return 'Главная страница'


@app.get('/user/admin')
async def admin_page() -> str:
    """
    Функция обработки запроса при обращении к странице администратора.
    :return: словарь с ответным сообщением.
    """
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}',)
async def user_id_page(user_id:int) -> str:
    """
    Функция обработки запроса при обращении к странице пользователя с конкретным id.
    :param user_id: идентификатор пользователя к станце которого идет запрос.
    :return: словарь с ответным сообщением.
    """
    return f'Вы вошли как пользователь № {user_id}'


@app.get('/user',)
async def user_info_page(username:str, age:int) -> str:
    """
    Функция обработки запроса при обращении к странице пользователя с передачей параметров.
    :param username: имя полбзователя;
    :param age: возраст пользователя.
    :return: словарь с ответным сообщением.
    """
    return f"Информация о пользователе. Имя: '{username}', Возраст: {age}"



if __name__ == "__main__":
    uvicorn.run("module_16_1:app", host='127.0.0.1', port=8000, reload=True)
