from settings import *

router = Router()

@router.message(F.text, Command('start'))
async def send_welcome(message: types.Message):
    from keyboards.home import home_kb
    # Starting message
    await message.reply("Привет! Выбери интересующую тебя опцию", reply_markup=home_kb())

