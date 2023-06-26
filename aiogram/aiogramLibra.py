from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv('.env')
token = os.environ.get('TOKEN')
bot = Bot(token)

dp = Dispatcher(bot)

# content_types=['photo', 'video', 'text', 'audio']
@dp.message_handler(content_types=['photo'])
async def start(message:types.Message):
    # await bot.send_message(message.chat.id, 'hello')
    # await message.answer('Hello')
    await message.reply('Hello')
    
    # await message.answ
    
@dp.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Site', url='https://google.com')
    item2 = types.InlineKeyboardButton('hi', callback_data='hi')
    markup.add(item1)
    markup.add(item2)
    await message.reply('hello', reply_markup=markup)

@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)
    
    
@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    item1 = types.KeyboardButton('site')
    # item2 = types.KeyboardButtonPollType('a')
    # item3 = types.KeyboardButtonRequestChat(message.chat.id, True)
    markup.add(item1)
    # markup.add(item2)
    await message.answer('hii',reply_markup=markup)
    # markup.add(item3)
    
executor.start_polling(dp)