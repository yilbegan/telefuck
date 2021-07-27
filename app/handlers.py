from aiogram import types
from .misc import dp, fuck
import random


@dp.message_handler()
async def main_handler(message: types.Message):
    bucket: dict = await dp.storage.get_bucket()
    bf_storage: str = bucket.get("bf_storage", "\1" * 10)
    stdin = (
        f"{message.text}\0"
        f"{bf_storage}\0"  # database
        f"{chr(random.randint(1, 10))}\0"  # random source
    )

    result = fuck.evaluate(stdin)
    parsed = {}
    for field in result.split("\0"):
        if not field:
            continue
        parsed[field[0]] = field[1:]

    if parsed.get("A"):
        await message.answer(parsed["A"])

    if parsed.get("D"):
        bucket["bf_storage"] = parsed["D"]
        await dp.storage.set_bucket(bucket)
