import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_URL = os.getenv("DATABASE_URL")  # postgresql://user:pass@host:port/dbname
ADMINS = [int(x) for x in os.getenv("ADMINS", "").split(",") if x]
