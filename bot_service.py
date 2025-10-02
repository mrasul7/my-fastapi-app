import asyncio
from aiogram import Bot, Dispatcher
from core.bot import bot
from db.psql.crud.crud import init_psql
from core.logger import bot_logger


dp = Dispatcher()

async def startup(bot: Bot) -> None:
    await init_psql()
    bot_logger.info("=== Bot started ===")

async def shutdown(bot: Bot) -> None:
    await bot.close()
    await dp.stop_polling()
    bot_logger.info("=== Bot stopped ===")


async def main() -> None:
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        bot_logger.info('Exit')