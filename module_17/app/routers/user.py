from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
from typing import List


router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    """
    Функция обработки запроса при обращении к странице с информацией о всех пользователях.
    :param db: база данных с информацией о пользователях.
    :return: список с пользователями.
    """
    users = db.scalars(select(User)).all()

    return users


@router.get('/user_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
    Функция обработки запроса при обращении к странице с информацией о конкретном пользователе по его id.
    :param db: база данных с информацией о пользователях;
    :param user_id: id пользователя информация о котором запрашивается.
    :return: информация о пользователе при его наличии в базе или ошибка 404.
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    
    return user


@router.get('/user_id/tasks')
async def user_by_id(db: Annotated[Session, Depends(get_db)], user_id: int):
    """
    Функция обработки запроса при обращении к странице с информацией о списке всех задач конкретном пользователе по его id.
    :param db: база данных с информацией о пользователях и задачах;
    :param user_id: id пользователя информация о списке задач которого запрашивается.
    :return: информация о списке задач пользователя при его наличии в базе или ошибка 404.
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    
    user_tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    
    return user_tasks


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser) -> dict:
    """
    Функция обработки запроса при отправке информации по пути для создания нового пользователя.
    :param db: база данных с информацией о пользователях;
    :param create_user: информация о создаваемом пользователе.
    :return: словарь с информацией о результатах создания нового пользователя.
    """
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)], update_user: UpdateUser, user_id: int) -> dict:
    """
    Функция обработки запроса при отправке информации для обновления данных о существующем пользователе.
    :param db: база данных с информацией о пользователях;
    :param update_user: редактируемая информация о существующем пользователе;
    :param user_id: id пользователя информация о котором будет отредактирована.
    :return: словарь с информацией о результатах редактирования информации пользователя или ошибка 404 при отсутствии пользователя в базе.
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    db.execute(update(User).where(User.id == user_id).values(firstname=update_user.firstname,
                                                             lastname=update_user.lastname,
                                                             age=update_user.age))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}


@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)], user_id: int) -> dict:
    """
    Функция обработки запроса при отправке информации для удаления пользователе из базы.
    :param db: база данных с информацией о пользователях;
    :param user_id: id пользователя информация о котором будет удалена.
    :return: словарь с информацией о результатах удаления пользователя или ошибка 404 при отсутствии пользователя в базе.
    """
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    # Удаляем информацию о задачах привязанных к удаляемому пользователю из таблицы - tasks
    db.execute(delete(Task).where(Task.user_id == user_id))
    # Удаляем информацию о пользователе из таблицы - users
    db.execute(delete(User).where(User.id == user_id))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User delete is successful!'}
