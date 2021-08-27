from aiogram import types
from .misc import dp, fuck
from .utils import create_image
import random
import io


@dp.message_handler()
async def main_handler(message: types.Message):
    bucket: dict = await dp.storage.get_bucket(user=message.from_user.id)
    bf_storage: str = bucket.get("bf_storage", "\1" * 10)
    stdin = (
        f"{message.text}\0"
        f"{bf_storage}\0"  # database
        f"{chr(random.randint(1, 10))}\0"  # random source
    )

    try:
        result = fuck.evaluate(stdin, limit=100000)
    except TimeoutError:
        return

    parsed = {}
    for field in result.split("\0"):
        if not field:
            continue
        parsed[field[0]] = field[1:]

    if parsed.get("D"):
        bucket["bf_storage"] = parsed["D"]
        await dp.storage.set_bucket(user=message.from_user.id, bucket=bucket)

    if parsed.get("I"):
        image = create_image(parsed["I"]).resize((630, 630))
        buffer = io.BytesIO()
        image.save(buffer, format="PNG")
        buffer.seek(0)
        await message.answer_photo(
            photo=types.InputFile(buffer, filename="brainfuck.png"),
            caption=parsed.get("A"),
        )

    elif parsed.get("A"):
        await message.answer(parsed["A"])
