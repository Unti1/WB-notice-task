from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def home_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Получить информацию по товару", callback_data='get_tovar'))
    builder.row(
        types.InlineKeyboardButton(
            text="Остановить оповещения",
            callback_data='stop_notice'),
        types.InlineKeyboardButton(
            text="Получить информацию из БД",
            callback_data='get_db_info')
    )

    return builder.as_markup()

def subscribe(articule):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Подписаться на рассылку", callback_data=f'subscribe_{articule}'))
    return builder.as_markup()
    