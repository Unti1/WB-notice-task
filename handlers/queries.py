from settings import *
from settings.states import BaseStates

router = Router()

@router.callback_query(F.data == 'get_data')
async def get_data(query: types.CallbackQuery, state:FSMContext):
    state.set_state(BaseStates.articule_input)
    query.answer(text='Введите артикул интересующего вас товара')

