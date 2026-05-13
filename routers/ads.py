import asyncio
from aiogram import Router
from database import get_id
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.exceptions import (
    TelegramForbiddenError,
    TelegramBadRequest
)

router = Router()

ADMIN_IDS = [
    5611541842,
]


def is_admin(user_id: int) -> bool:
    return user_id in ADMIN_IDS


@router.message(Command("ads"))
async def send_ads(message: Message):
    if not is_admin(message.from_user.id):
        return

    args = message.text.split(maxsplit=1)

    if len(args) < 2:
        await message.answer(
            "Usage:\n/ads Hello everyone"
        )
        return

    ad_text = args[1]

    users = get_id()

    success = 0
    failed = 0

    for user in users:
        user_id = user[0]

        try:
            await message.bot.send_message(
                chat_id=user_id,
                text=ad_text
            )
            success += 1

            await asyncio.sleep(0.05)

        except (
                TelegramForbiddenError,
                TelegramBadRequest
        ):
            failed += 1

    await message.answer(
        f"Ads sent\n\n"
        f"Success: {success}\n"
        f"Failed: {failed}"
    )


# ==========================
# SEND TO ONE USER
# ==========================
@router.message(Command("send"))
async def send_to_user(message: Message):
    if not is_admin(message.from_user.id):
        return

    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.answer(
            "Usage:\n/send user_id message"
        )
        return

    try:
        user_id = int(args[1])
    except ValueError:
        await message.answer(
            "Invalid user_id"
        )
        return

    text = args[2]

    try:
        await message.bot.send_message(
            chat_id=user_id,
            text=text
        )

        await message.answer(
            f"Message sent to {user_id}"
        )

    except TelegramForbiddenError:
        await message.answer(
            "User blocked the bot"
        )

    except TelegramBadRequest:
        await message.answer(
            "Invalid user_id"
        )
