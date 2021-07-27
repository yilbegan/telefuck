from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.executor import start_webhook
from pathlib import Path
from .brainfuck import Brainfuck
from . import config

WEBHOOK_HOST = f'https://{config.HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{config.TELEGRAM_TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = config.PORT
SCRIPT = Path(__file__).parent.parent / "main.bf"
fuck = Brainfuck(SCRIPT.open().read())

bot = Bot(config.TELEGRAM_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


async def on_startup(_: Dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates=True)


def main():
    # noinspection PyUnresolvedReferences
    import app.handlers

    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        skip_updates=True,
        on_startup=on_startup,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
