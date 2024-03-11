from tools.bd import *


# Определение класса модели для WB_item
class WB_item(Base):
    __tablename__ = 'wb_items'  # Имя таблицы в базе данных
    
    # Определение столбцов таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)  # Название товара
    article = Column(String)  # Артикул товара
    price = Column(Float)  # Цена товара
    rating = Column(Float)  # Рейтинг товара
    stock = Column(Integer)  # Количество товара на всех складах

    def __init__(self, name, article, price, rating, stock):
        self.name = name
        self.article = article
        self.price = price
        self.rating = rating
        self.stock = stock