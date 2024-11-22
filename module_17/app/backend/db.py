from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Создаем движек
engin = create_engine('sqlite:///taskmanager.db', echo=True)

# Создаем сессию
SessionLocal = sessionmaker(bind=engin)

class Base(DeclarativeBase):
    pass
