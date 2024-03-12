from settings import *
from handlers import commands, messages, queries
from tools.bd import *


async def main_run():
    bot = Bot(token = config['telegram']['token'])
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(messages.router, commands.router, queries.router)
    session = database_init()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main_run())
