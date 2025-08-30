import asyncio
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramForbiddenError

from config import BOT_TOKEN
from database import init_db
from handlers import routers
from utils.logger import logger




async def main():
    await init_db()
    
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    await bot.delete_webhook(drop_pending_updates=True)

    # Register all routers
    for r in routers:
        dp.include_router(r)

    logger.info("Bot started 🚀")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
