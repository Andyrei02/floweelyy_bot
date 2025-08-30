from aiogram.types import User
from database import get_pool

async def save_user(tg_user: User):
    pool = await get_pool()
    async with pool.acquire() as conn:
        await conn.execute("""
            INSERT INTO users (telegram_id, username, full_name, language_code)
            VALUES ($1, $2, $3, $4)
            ON CONFLICT (telegram_id) DO UPDATE
            SET username = EXCLUDED.username,
                full_name = EXCLUDED.full_name,
                language_code = EXCLUDED.language_code
        """, tg_user.id, tg_user.username, tg_user.full_name, tg_user.language_code)
