from aiogram import Router
from aiogram.types import Message

other_router = Router()

other_router.message()
async def other_message_handler(message: Message):
    await message.answer("Нажмите на кнопку ниже, чтобы выбрать случайный мод")