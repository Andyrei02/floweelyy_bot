from aiogram import Router, types
from aiogram.filters import Command
from config import ADMINS

router = Router()

@router.message(Command("admin"))
async def cmd_admin(message: types.Message):
    if message.from_user.id in ADMINS:
        await message.answer("✅ Welcome, Admin! Here will be your panel.")
    else:
        await message.answer("⛔ You are not an admin.")
