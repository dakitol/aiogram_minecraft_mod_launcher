from dataclasses import dataclass
from environs import Env

@dataclass
class LogConfig():
    log_level: str
    log_format: str

@dataclass
class BotConfig():
    bot_token: str
    bot_parse_mode: str

@dataclass
class Config():
    logConfig: LogConfig
    botConfig: BotConfig

def get_config(path: str = ".env"):
    env = Env()
    env.read_env(path=path)
    return Config(
        logConfig=LogConfig(
            log_level=env("LOG_LEVEL"),
            log_format=env("LOG_FORMAT")
        ),
        botConfig=BotConfig(
            bot_token=env("BOT_TOKEN"),
            bot_parse_mode=env("BOT_PARSE_MODE")
        )
    )