import telebot
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv('.env')


bot = telebot.TeleBot(os.environ.get('TOKEN'))
key = os.environ.get('API')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, рад тебя видеть, напиши название своего города")
    

@bot.message_handler(content_types = ['text'])
def get_weather(message):
    city = message.text.strip().lower() 
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&units=metric')   
    
    if res.status_code == 200:
        data = json.loads(res.text) 
        temp = data["main"]["temp"]
        # bot.reply_to(message, data)
        bot.reply_to(message, f'Сейчас погода: {temp}')

        image = 'sunny.png' if temp > 5.0 else 'sun.jpg'
        file = open("./static/"+image,'rb')
        bot.send_photo(message.chat.id,file)
    else:
        bot.reply_to(message, 'Город указан не верно')
    
    
bot.polling(none_stop=True)