from tools.db import *
import json

# Определение класса модели для WB_item
class WB_item(Base):
    __tablename__ = 'wb_items'  # Имя таблицы в базе данных
    
    # Определение столбцов таблицы
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    name = Column(String)  # Название товара
    article = Column(String)  # Артикул товара
    price = Column(Float)  # Цена товара
    rating = Column(Float)  # Рейтинг товара
    stock = Column(JSON)  # Количество товара на всех складах

    def __init__(self, user_id, **kwargs):
        self.user_id = int(user_id)
        self.name: str = kwargs.get('name', '')
        self.article: int = str(kwargs.get('id', ''))
        self.price: float = float(kwargs.get('salePriceU')) if kwargs.get('salePriceU') else kwargs.get('priceU','0')
        self.rating: float = float(kwargs.get('reviewRating', ''))
        sizes: list[dict] = kwargs.get('sizes') 
        self.stock: dict = self.get_stocks(sizes)

    def get_stocks(self, sizes):
        if sizes != []:
            return dict(
                        map(
                            lambda x: (
                                x.get('name'), 
                                ' - '.join(map(lambda stock: f"Склад[{stock.get('wh')}] - {stock.get('qty')} шт." ,x.get('stocks'))) if x.get('stocks') != [] else '0'
                                    ),
                                sizes
                                )
                            )
        else: 
            return ''

    def __str__(self):
        import json
        return f'Товар: {self.name}\n[{self.article}]\nЦена:{self.price}\nРейтинг:{self.rating}\nВ наличии есть размеры: {json.dumps(self.stock, ensure_ascii=False, indent=4)}'
    
