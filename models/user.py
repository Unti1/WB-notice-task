from tools.db import *

# Определение класса модели для WB_item
class User(Base):
    __tablename__ = 'user_subscribes'  # Имя таблицы в базе данных
    
    # Определение столбцов таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)  # User id in TG 
    article = Column(Integer)  # Item article

    def __init__(self, user_id, article):
        self.user_id = user_id
        self.article = article