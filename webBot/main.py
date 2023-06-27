from aiogram import Bot, Dispatcher, executor, types
import os
from dotenv import load_dotenv
from aiogram.types.web_app_info import WebAppInfo

load_dotenv('../.env')
token = os.environ.get('TOKEN')

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='github.com/NiceeeTry/TestBot/blob/2e16144e0e917797001789d247ee4599aab80e12/webBot/index.html'))
    markup.add(item1)
    await message.answer('Yooooo',reply_markup=markup)
    

executor.start_polling(dp)