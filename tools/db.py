from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import *


# Определение базового класса
Base = declarative_base()

def database_init():
    from models import User, WB_item
    # Создание сессии базы данных
    engine = create_engine(DATABASE_URL, echo=True)  # Здесь можно указать другой URL базы данных
    Base.metadata.create_all(engine)  # Создание таблицы, если она еще не существует
    Session = sessionmaker(bind=engine)
    session = Session()
    return session