from aiogram import Router, Bot, F
from aiogram.types import Message, URLInputFile
from aiogram.filters import Command
from service.mod_randomizer import get_random_mod, MinecraftMod

import logging

from keyboards.keyboards import create_game_icons_markup

logger = logging.getLogger(__name__)

user_router = Router()

@user_router.message(Command("start"))
async def process_command_start(message: Message):
    await message.answer(
        text="<b>Привет!</b> \n" \
        "Этот бот умеет рандомизировать майнкрафт мод, учитывая ваши настройки\n" \
        "Например: Ядро(🛠️Forge/Fabric📜), Версию и многое другое...",
        reply_markup=create_game_icons_markup()
    )

@user_router.message(Command("random"))
async def process_command_random(message: Message):
    try:
        mod_info: MinecraftMod = await get_random_mod(["forge", "neoforge"], "1.21.1")
        await message.answer_photo(
            photo=URLInputFile(mod_info.icon_url),
            caption=f"<b>{mod_info.name}</b>\n<a href='{mod_info.modrinth_url}'>➡️СКАЧАТЬ ЗДЕСЬ⬅️</a>"
        )
    except Exception as e:
        logger.error(e)