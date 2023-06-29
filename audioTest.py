import aiogram

from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv('.env')
token = os.environ.get('TOKEN')
bot = Bot(token)

dp = Dispatcher(bot)