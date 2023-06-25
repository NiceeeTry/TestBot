import telebot
from telebot import types
import os
from dotenv import load_dotenv
import webbrowser

load_dotenv('.env')

bot = telebot.TeleBot(os.environ.get('TOKEN'))



@bot.message_handler(commands=['start'])
def start(message):
    # second type of buttons
    markup = types.ReplyKeyboardMarkup()
    item1 = types.KeyboardButton('Перейти на сайт')
    item2 = types.KeyboardButton('Удалить фото')
    item3 = types.KeyboardButton('Изменить')
    markup.add(item1)
    markup.add(item2,item3)
    
    file = open('tg.jpeg','rb')
    bot.send_photo(message.chat.id,file, reply_markup=markup)
    # bot.send_audio(message.chat.id,file, reply_markup=markup)
    #bot.send_video(message.chat.id,file, reply_markup=markup)    
    bot.register_next_step_handler(message,on_click)
    
def on_click(message):
    if message.text=='Перейти на сайт':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'delted')
# Website handling in bot. Opening sites.
@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://google.com')

# Handling pictures and other datatype
@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # First type of BOTTONS -> REPLY
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('Перейти на сайт', url='https://google.com')
    item2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete' )
    item3 = types.InlineKeyboardButton('Изменить', callback_data='edit')
    # reply option in a column - default
    markup.add(item1)
    # Reply options in a row markup.row(item)
    markup.add(item2,item3)
    bot.reply_to(message, 'Nicee pic',reply_markup = markup)
    

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    # delete messages
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data =='edit':
        # edit messages
        bot.edit_message_text('Edit text',callback.message.chat.id, callback.message.message_id)
        
        


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id,'<b>help</b><i><u>information</u></i>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower()=='id':
        bot.reply_to(message, f'Your ID is {message.from_user.id}')

# bot.polling(none_stop=True)
bot.infinity_polling()