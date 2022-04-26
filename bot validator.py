import logging
import settings
from aiogram import executor
from handlers import client


async def start_bot(_):
    print("Бот вышел в онлайн")

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO)
    client.register_handlers_client(settings.dp)
    executor.start_polling(settings.dp, skip_updates=True, on_startup=start_bot)



