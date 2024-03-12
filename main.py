from settings import *
from handlers import commands, messages, queries
from tools.db import *
from apscheduler.schedulers.asyncio import AsyncIOScheduler



async def main_run():
    bot = Bot(token=config['telegram']['token'])
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(messages.router, commands.router, queries.router)
    bot.db_control = database_init()


    from handlers.messages import subscribers_sender
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler._logger.setLevel(logging.ERROR) # Отключаем логирование для очереди
    scheduler.add_job(subscribers_sender, trigger = 'interval', seconds = 300,
                      kwargs={"bot" : bot})
    scheduler.start()
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main_run())