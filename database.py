import asyncpg
from config import DB_URL

pool: asyncpg.Pool | None = None

async def init_db():
    """Create connection pool and ensure base tables exist."""
    global pool
    pool = await asyncpg.create_pool(dsn=DB_URL, min_size=1, max_size=5)

    async with pool.acquire() as conn:
        await conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id BIGSERIAL PRIMARY KEY,
            telegram_id BIGINT UNIQUE NOT NULL,
            username TEXT,
            full_name TEXT,
            language_code VARCHAR(5),
            created_at TIMESTAMP DEFAULT NOW()
        );
        """)

async def get_pool() -> asyncpg.Pool:
    return pool



# import asyncpg
# from config import DB_URL

# pool: asyncpg.Pool = None

# async def init_db():
#     global pool
#     pool = await asyncpg.create_pool(dsn=DB_URL, min_size=1, max_size=5)

# async def get_conn():
#     return pool


# # utils/translations.py
# # from database import get_conn

# async def get_translation(key: str, lang: str = "en") -> str:
#     conn = await get_conn()
#     row = await conn.fetchrow(
#         "SELECT text FROM translations WHERE key=$1 AND lang_code=$2",
#         key, lang
#     )
#     return row["text"] if row else key

# # utils/users.py
# from aiogram.types import User
# # from database import get_conn

# async def save_user(tg_user: User):
#     conn = await get_conn()
#     await conn.execute("""
#         INSERT INTO users (telegram_id, username, full_name, language_code)
#         VALUES ($1, $2, $3, $4)
#         ON CONFLICT (telegram_id) DO UPDATE
#         SET username = EXCLUDED.username,
#             full_name = EXCLUDED.full_name,
#             language_code = EXCLUDED.language_code
#     """, tg_user.id, tg_user.username, tg_user.full_name, tg_user.language_code)


# # import asyncio 
# # import asyncpg 
# # from aiogram import Bot, Dispatcher, types 
# # from aiogram.filters import Command 
# # BOT_TOKEN = "YOUR_BOT_TOKEN" 
# # DB_DSN = "postgresql://user:password@host:port/dbname" 

# async def init_db():
#     conn = await asyncpg.connect(DB_URL)
#     await conn.execute("""
#         CREATE TABLE IF NOT EXISTS users (
#             id BIGSERIAL PRIMARY KEY, 
#             telegram_id BIGINT UNIQUE NOT NULL, 
#             username TEXT, 
#             full_name TEXT, 
#             phone TEXT, 
#             language_code VARCHAR(5) DEFAULT 'en', 
#             created_at TIMESTAMP DEFAULT NOW() 
#         ); 
#         CREATE TABLE IF NOT EXISTS languages ( 
#             code VARCHAR(5) PRIMARY KEY, 
#             name TEXT NOT NULL 
#         ); 
#         CREATE TABLE IF NOT EXISTS translations ( 
#             key TEXT NOT NULL, 
#             lang_code VARCHAR(5) REFERENCES languages(code), 
#             text TEXT NOT NULL, 
#             PRIMARY KEY (key, lang_code) 
#         ); 
#     """) 
#     await conn.close() 
# # async def get_translation(conn, key, lang_code): 
# #     row = await conn.fetchrow( 
# #         "SELECT text FROM translations WHERE key=$1 AND lang_code=$2", 
# #         key, lang_code 
# #     ) 
# #     return row["text"] if row else key

# # # fallback to key if missing 
# # async def save_user(conn, tg_user: types.User): 
# #     await conn.execute(""" 
# #         INSERT INTO users (telegram_id, username, full_name, language_code) 
# #         VALUES ($1, $2, $3, $4) 
# #         ON CONFLICT (telegram_id) DO UPDATE 
# #         SET username = EXCLUDED.username, 
# #         full_name = EXCLUDED.full_name, 
# #         language_code = EXCLUDED.language_code 
# #         """, tg_user.id, tg_user.username, tg_user.full_name, tg_user.language_code) 

# # async def main(): 
# #     await init_db() 
# #     bot = Bot(token=BOT_TOKEN) 
# #     dp = Dispatcher() 

# #     @dp.message(Command("start")) 
# #     async def start_handler(message: types.Message): 
# #         conn = await asyncpg.connect(DB_DSN)
# #         await save_user(conn, message.from_user) 
# #         text = await get_translation(conn, "start_message", message.from_user.language_code or "en") 
# #         await conn.close() 
# #         await message.answer(text) 
# #         await dp.start_polling(bot) 


# # if __name__ == "__main__": 
# #         asyncio.run(main())
