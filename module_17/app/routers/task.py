from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify
from typing import List


router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    """
    Функция обработки запроса при обращении к странице с информацией о всех задачах.
    :param db: база данных с информацией о задачах.
    :return: список с задачами.
    """
    tasks = db.scalars(select(Task)).all()

    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    """
    Функция обработки запроса при обращении к странице с информацией о конкретной задаче по её id.
    :param db: база данных с информацией о задачах;
    :param task_id: id задачи информация о которой запрашивается.
    :return: информация о задаче при её наличии в базе или ошибка 404.
    """
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    
    return task


@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)], user_id: int, create_task: CreateTask) -> dict:
    """
    Функция обработки запроса при отправке информации по пути для создания новой задачи.
    :param db: база данных с информацией о задачах;
    :param user_id: id пользователя к которому привязывается создаваемая задача;
    :param create_task: информация о создаваемой задаче.
    :return: словарь с информацией о результатах создания новой задачи или ошибка 404 при отсутствии пользователя к которому привязывается задача в базе.
    """
    # Проверяем наличия пользователя в таблице users
    user = db.scalar(select(User).where(User.id == user_id))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )

    # Создаем задачу с привязкой к пользователю по id
    db.execute(insert(Task).values(title=create_task.title,
                                   content=create_task.content,
                                   priority=create_task.priority,
                                   user_id=user_id,
                                   slug=slugify(create_task.title)))
    db.commit()

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)], update_task: UpdateTask, task_id: int) -> dict:
    """
    Функция обработки запроса при отправке информации для обновления данных о существующей задаче.
    :param db: база данных с информацией о задачах;
    :param update_task: редактируемая информация о существующей задаче;
    :param task_id: id задачи информация о которой будет отредактирована.
    :return: словарь с информацией о результатах редактирования информации задачи или ошибка 404 при отсутствии задачи в базе.
    """
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )

    db.execute(update(User).where(Task.id == task_id).values(title=update_task.title,
                                                             content=update_task.content,
                                                             priority=update_task.priority,
                                                             slug=slugify(update_task.title)))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    """
    Функция обработки запроса при отправке информации для удаления задачи из базы.
    :param db: база данных с информацией о задачах;
    :param task_id: id задачи информация о которой будет удалена.
    :return: словарь с информацией о результатах удаления задачи или ошибка 404 при отсутствии задачи в базе.
    """
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task was not found'
        )
    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
