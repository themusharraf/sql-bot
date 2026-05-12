from aiogram import Router
from aiogram.types import Message
from database import add_user
from aiogram.filters.command import CommandStart

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    add_user(message.from_user.full_name, message.from_user.username, message.from_user.id)
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}")
