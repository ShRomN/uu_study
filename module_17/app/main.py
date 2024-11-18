from fastapi import FastAPI
from app.routers import task, user

app = FastAPI()

@app.get('/')
async def main_page() -> dict:
    """
    Функция обработки запроса при обращении к главной странице.
    :return: ***.
    """
    return {'message': 'Welcome to Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)
