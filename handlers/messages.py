from settings import *
from settings.states import BaseStates
from models import *


router = Router()


@router.message(BaseStates.articule_input, F.text)
async def articule_input_access(message: types.Message, state:FSMContext):
    from tools.parser import get_info_for_article
    from keyboards.main_kb import subscribe
    import json

    article = re.match(r'\d+', message.text)[0]
    result = await get_info_for_article(article)
    
    data = WB_item(message.chat.id,**result[0])
    message.bot.db_control.add(data)

    print(str(WB_item(**result[0])))
    for product in data:
        await message.reply(str(data),reply_markup=subscribe(article))


async def subscribers_sender(bot: Bot):
    from tools.parser import get_info_for_article
    subscribers = bot.db_control.query(User).all()
    for subscriber in subscribers:
        result = await get_info_for_article(subscriber.article)
        item = WB_item(subscriber.user_id, **result[0])
        await bot.send_message(subscriber.user_id, str(item))