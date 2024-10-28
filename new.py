from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeDefault, MenuButtonDefault
import asyncio
import aiohttp

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeDefault, MenuButtonDefault
import asyncio

API_TOKEN = '7810663971:AAH5R2-0rUhMz-ymexydljy2OCGiRcGmtXY'
PROXY = 'http://hiyktu8arq-res-country-RU-state-468898-city-468902-hold-session-session-671eada282dcc:8mMiao2ZPyWlwYPH@93.190.142.57:9999'  # Замените на ваш прокси


async def remove_all_commands(bot: Bot):
    await bot.delete_my_commands(scope=BotCommandScopeDefault())
    await bot.set_chat_menu_button(menu_button=MenuButtonDefault())
    print("Старые команды и меню удалены.")


async def main():
    # Создаем бот с прокси
    bot = Bot(token=API_TOKEN)

    try:
        await remove_all_commands(bot)
    finally:
        await bot.session.close()
        print("Сессия закрыта.")


if __name__ == "__main__":
    asyncio.run(main())


