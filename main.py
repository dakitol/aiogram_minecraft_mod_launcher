import asyncio
from config.config import get_config, Config
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from routers.user_router import user_router

config: Config = get_config()

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=config.logConfig.log_level,
    format=config.logConfig.log_format
)

async def main():
    logger.info("Bot is starting...")

    bot: Bot = Bot(
        token=config.botConfig.bot_token,
        default=DefaultBotProperties(
            parse_mode=eval("ParseMode."+config.botConfig.bot_parse_mode)
        )
    )

    dp: Dispatcher = Dispatcher()
    dp.include_router(user_router)

    logger.info("Bot initialized!")

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    

try:
    asyncio.run(main())
except KeyboardInterrupt:
    logger.info("Bot was stopped!")