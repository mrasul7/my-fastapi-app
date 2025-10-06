from aiogram import Bot, Dispatcher
from core.bot import bot
from db.psql.crud.crud import init_psql
from core.logger import bot_logger
from bot.handlers.commands import router as user_router

import asyncio

dp = Dispatcher()
dp.include_router(user_router)

async def startup(bot: Bot) -> None:
    await init_psql()
    bot_logger.info("=== Bot started ===")

async def shutdown(bot: Bot) -> None:
    await bot.session.close()
    await dp.stop_polling()
    bot_logger.info("=== Bot stopped ===")


async def main() -> None:
    dp.startup.register(startup)
    dp.shutdown.register(shutdown)

    try:
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        bot_logger.info('Выход')
    except Exception as e:
        bot_logger.error(f'Прозошла ошибка: {e}')
    finally:
        await shutdown(bot)


if __name__ == "__main__":
    asyncio.run(main())