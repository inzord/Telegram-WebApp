import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from backend.app.core.settings import settings

bot = Bot(token=settings.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)


@dp.message()
async def handle_birth_date(message: types.Message):
    username = message.from_user.username or "guest"
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[
        types.InlineKeyboardButton(
            text="Перейти в WebApp",
            url=f"{settings.FASTAPI_BASE_URL}/page_for/{username}"
        )
    ]])
    await message.answer(
        "Нажмите на кнопку ниже, чтобы перейти в WebApp и узнать важную информацию по этому поводу:",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
