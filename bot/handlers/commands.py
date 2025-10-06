from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from sqlalchemy import select
from core.psql import async_session_maker
from core.logger import bot_logger
from db.psql.models.models import User


import bot.templates.keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    if message.from_user is None:
        await message.answer("Не удалось получить информацию о пользователе")
        return None
    async with async_session_maker() as session:
        try:
            result = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
            db_user = result.scalar_one_or_none()
            if not db_user:
                new_user = User(
                    telegram_id=message.from_user.id,
                    name=message.from_user.first_name,
                    username=message.from_user.username,
                    created_at=message.date
                )
                session.add(new_user)
                await session.commit()
                await message.answer("Привет, отправьте ваш номер телефона:", reply_markup=kb.share_phone_kb)
        except Exception:
            await session.rollback()
            await message.answer("Произошла ошибка при обработке запроса")

@router.message(F.contact)
async def accept_number(message: Message) -> None:
    bot_logger.info(f"Contact received: {message.contact}")
    if message.from_user is None:
        await message.answer("Не удалось идентифицировать пользователя")
        return None
    if message.contact is None:
        await message.answer("Контактные данные не найдены")
        return None
    
    phone_number = message.contact.phone_number
    async with async_session_maker() as session:
        try:
            if phone_number:
                result = await session.execute(select(User).where(User.telegram_id == message.from_user.id))
                db_user = result.scalar_one_or_none()
                if db_user:
                    db_user.phone_number = phone_number
                    await session.commit()
                    await message.answer("Данные приняты. Спасибо!", reply_markup=kb.my_data_kb)
                else:
                    await message.answer("Пользователь не найден")
            else:
                await message.answer("Некорректный номер телефона")
        except Exception:
            await session.rollback()
            await message.answer("Произошла ошибка при обработке запроса")


@router.callback_query(F.data == "my_data")
async def show_my_data(callback: CallbackQuery) -> None:
    user_id = callback.from_user.id
    async with async_session_maker() as session:
        try:
            result = await session.execute(select(User).where(User.telegram_id == user_id))
            db_user = result.scalar_one_or_none()
            if db_user:
                message_text = (
                    f"Telegram ID: {db_user.telegram_id}\n"
                    f"Телефон: +{db_user.phone_number}\n"
                    f"Имя: {db_user.name}\n"
                    f"Username: @{db_user.username}\n"
                    f"Дата запуска бота: {db_user.created_at.astimezone().strftime('%d.%m.%Y %H:%M')}"
                )
            else:
                message_text = "Данные не найдены"
            await callback.message.edit_text(message_text, reply_markup=kb.back_kb)
            await callback.answer()
        except Exception:
                await session.rollback()
                await message.answer("Произошла ошибка при обработке запроса")
    
    
@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: CallbackQuery) -> None:
    await callback.message.edit_text("Данные приняты. Спасибо!", reply_markup=kb.my_data_kb)
    await callback.answer()

