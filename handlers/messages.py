from settings import *
from settings.states import BaseStates
router = Router()


@router.message(BaseStates.articule_input)
async def articule_input_access(message: types.Message, state:FSMContext):
    from tools.parser import get_info_for_article
    article = re.match('/d+')[0]
    print(get_info_for_article(f'https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}'))
