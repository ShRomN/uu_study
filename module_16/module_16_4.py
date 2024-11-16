from fastapi import FastAPI, Path, Body, HTTPException
from typing import Annotated, List
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Импровизированная база
users = []

class User(BaseModel):
    """
    Класс содержащий информацию о кафе.
    """
    id: int
    username: str = 'default_name'
    age: int = -1

    def __eq__(self, other):
        """
        Метод сравнения объектов по id.
        """
        return self.id == other.id



@app.get('/users')
async def get_users() -> List[User]:
    """
    Функция обработки запроса при обращении к странице с пользователями.
    :return: список с информацией о пользователях в базе.
    """
    return users


@app.post('/user/{username}/{age}')
async def post_user(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                         age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> User:
    """
    Функция обработки запроса добавления нового пользователя в базу.
    :param username: имя нового пользователя;
    :param age: возраст нового пользователя.
    :return: строка с ответным сообщением.
    """
    id = users[-1].id + 1 if users else 1
    user = User(id=id, username= username, age=age)
    users.append(user)
    return user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)],
                       username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
                       age: Annotated[int, Path(ge=18, le=120, description='Enter age', example=24)]) -> User:
    """
    Функция обработки запроса обновления сведений о пользователе в базе.
    :param user_id: идентификатор пользователя данные о котором обновляются;
    :param username: имя пользователя;
    :param age: возраст пользователя.
    :return: строка с ответным сообщением.
    """
    try:
        f_user = User(id=user_id)

        if f_user in users:
            edit_user = users[users.index(f_user)]
            edit_user.username = username
            edit_user.age = age
        else:
            raise IndexError()

        return edit_user
    
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example=1)]) -> User:
    """
    Функция обработки запроса удаления пользователя из базы.
    :param user_id: идентификатор удаляемого пользователя.
    :return: данные о удаленном пользователе.
    """
    try:
        f_user = User(id=user_id)

        if f_user in users:
            deleting_user = users.pop(users.index(f_user))
        else:
            raise IndexError()
        
        return deleting_user

    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')



if __name__ == "__main__":
    uvicorn.run("module_16_4:app", host='127.0.0.1', port=8000, reload=True)
