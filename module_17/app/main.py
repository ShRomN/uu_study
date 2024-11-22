from fastapi import FastAPI
from app.routers import task, user
import uvicorn


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


if __name__ == "__main__":
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)