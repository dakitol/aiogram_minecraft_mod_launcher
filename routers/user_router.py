from aiogram import Router, Bot, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.enums import ContentType, DiceEmoji

from keyboards.keyboards import create_game_icons_markup

user_router = Router()

@user_router.message(Command("start"))
async def process_command_start(message: Message):
    await message.answer(
        text="<b>Привет!</b> \n" \
        "Этот бот умеет рандомизировать майнкрафт мод, учитывая ваши настройки\n" \
        "Например: Ядро(🛠️Forge/Fabric📜), Версию и многое другое...",
        reply_markup=create_game_icons_markup()
    )

@user_router.message(F.dice)
async def dice_handler(message: Message):
    dice = message.dice
    
    if dice.emoji == DiceEmoji.DICE:
        await message.answer(f"Вы бросили кость! 🎲\nВыпало: {dice.value}")
    
    elif dice.emoji == DiceEmoji.BASKETBALL:
        await message.answer(f"Баскетбол! 🏀\nОчки: {dice.value}")
    
    elif dice.emoji == DiceEmoji.FOOTBALL:
        await message.answer(f"Футбол! ⚽\nОчки: {dice.value}")
    
    elif dice.emoji == DiceEmoji.SLOT_MACHINE:
        await message.answer(f"Игровой автомат! 🎰\nКомбинация: {dice.value}")
    
    elif dice.emoji == DiceEmoji.BOWLING:
        await message.answer(f"Боулинг! 🎳\nСбито кеглей: {dice.value}")
    
    elif dice.emoji == DiceEmoji.DART:
        await message.answer(f"Дартс! 🎯\nПопадание: {dice.value}")