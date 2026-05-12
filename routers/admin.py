from aiogram import Router, F
from aiogram.types import Message
from database import get_users
from aiogram.filters.command import Command

router = Router()

@router.message(Command("show_users"))
async def show_users(message:Message):
    users = get_users()
    for x in users:
        await message.answer(f"name: {x[1]}\nusername: {x[2]}\ntelegram_id: {x[3]}")
