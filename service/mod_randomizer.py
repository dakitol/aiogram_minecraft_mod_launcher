import httpx, asyncio
import logging
from dataclasses import dataclass
from random import randint

logger = logging.getLogger(__name__)
logging.basicConfig(level="INFO", format="%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

@dataclass
class MinecraftMod:
    name: str
    icon_url: str

async def get_random_mod(gamecores: list[str], version: str) -> MinecraftMod:
    cores = ",".join( f'"categories:{core}"' for core in gamecores)
    count_url = f'https://api.modrinth.com/v2/search?limit=1&facets=[[{cores}], ["versions:{version}"], ["project_type:mod"]]&index=downloads'
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(count_url)
            response.raise_for_status()
            
            count_data: dict = response.json()

            mods_count = int(count_data["total_hits"])

            mod_number = randint(0, mods_count-1)

            url = f'https://api.modrinth.com/v2/search?limit=1&offset={mod_number}&facets=[[{cores}], ["versions:{version}"], ["project_type:mod"]]&index=downloads'
            
            response = await client.get(url)
            response.raise_for_status()

            mod_data: dict = response.json()

            return MinecraftMod(
                name=mod_data["hits"][0]["title"],
                icon_url=mod_data["hits"][0]["icon_url"]
            )

        except httpx.HTTPError as e:
            logger.error(f"Ошибка HTTP: {e}")
        except Exception as e:
            logger.error(f"Произошла ошибка: {e}")


async def main():
    mod = await get_random_mod(["forge", "neoforge"], "1.21.1")
    print(mod)
asyncio.run(main())