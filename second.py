import telebot
from telebot import types
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv('.env')

bot = telebot.TeleBot(os.environ.get('TOKEN'))
name = None


@bot.message_handler(commands=['start'])
def start(message):
    # sqlite3 as a database 
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_incremect primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    
    bot.send_message(message.chat.id, 'Hi, lets register\nEnter your name')
    bot.register_next_step_handler(message, user_name)
    
def user_name(message):
    global name 
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Enter a password: ')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    
    cur.execute(f"INSERT INTO users (name, pass) VALUES('%s', '%s')" % (name, password))
    conn.commit()
    cur.close()
    conn.close()
    
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton('List of users', callback_data='users')
    markup.add(item1)
    bot.send_message(message.chat.id, 'You are registered',reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)

@bot.callback_query_handler(func = lambda call:True)
def callback(call):
    if call.data == 'users':
        conn = sqlite3.connect('bot.sql')
        cur = conn.cursor()
            
        cur.execute("SELECT * FROM users")
        users = cur.fetchall()
        
        info = ''
        for i in users:
            info += f'Имя: {i[1]}, Пароль: {i[2]}\n'
        
        cur.close()
        conn.close()
        
        bot.send_message(call.message.chat.id, info)

bot.polling(none_stop=True)