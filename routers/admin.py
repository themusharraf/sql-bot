from aiogram import Router, F
from aiogram.types import Message
from database import get_users, delete_user
from aiogram.filters.command import Command

router = Router()


@router.message(Command("show_users"))
async def show_users(message: Message):
    users = get_users()

    text = "\n\n".join(
        f"name: {x[1]}\n"
        f"username: @{x[2]}\n"
        f"telegram_id: {x[3]}"
        for x in users
    )

    await message.answer(text)


@router.message(Command("delete_user"))
async def user_message_id(message: Message):
    await message.answer("Delete qilmoqchi bo'lgan user idsini yuboring!")

    @router.message(F.text)
    async def user_del(message: Message):
        delete_user(message.text)
        await message.answer("User o'chirib tashlandi!")
