import asyncio
import logging
import pprint

from environs import Env
from kwork import Kwork
from kwork.types import Actor

env = Env()
env.read_env()

kwork_login = env("KWORK_LOGIN")
kwork_password = env("KWORK_PASSWORD")


logging.basicConfig(level=logging.INFO)


async def main():
    api = Kwork(login=kwork_login, password=kwork_password)
    try:
        me: Actor = await api.get_me()
        # Получение своего профиля
        pprint.pprint(me)
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
