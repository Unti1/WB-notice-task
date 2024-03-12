from settings import *
from settings.states import BaseStates
from models import *

router = Router()

@router.callback_query(F.data == 'get_tovar')
async def get_data(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(BaseStates.articule_input)
    await callback.message.answer(text='Введите артикул интересующего вас товара')

@router.callback_query(F.data == 'stop_notice')
async def stop_notice(callback: types.CallbackQuery):
    user = callback.bot.db_control.query(User).filter(User.user_id == callback.message.chat.id).first()
    callback.bot.db_control.delete(user)
    callback.bot.db_control.commit()
    await callback.message.reply('Вы были отписаны от рассылки на ранее подписанные артикулы WB.')

@router.callback_query(F.data == 'get_db_info')
async def get_from_db(callback: types.CallbackQuery):
    five_last: list = callback.bot.db_control.query(WB_item)\
        .filter(WB_item.user_id == callback.message.chat.id)\
        .order_by(WB_item.id.desc())\
        .limit(5)\
        .all()
    
    for item in five_last:
        await callback.message.reply(str(item))

@router.callback_query(F.data.startswith('subscribe_'))
async def stop_notice(callback: types.CallbackQuery):
    article = callback.data.split('_')[1]
    user_id = callback.message.chat.id
    callback.bot.db_control.add(User(user_id=user_id, article=article))
    callback.bot.db_control.commit()
    await callback.message.reply(f'Вы были подписаны на {article}')