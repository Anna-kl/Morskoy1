import telebot
from telebot import types
import sys
import os
from play import Play
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
bot_tb = telebot.AsyncTeleBot('1369972878:AAEuB4oYgildqi5S7s2oEZcHVHhDtYx2TqY')
from models_base import DB
base=DB()
@bot_tb.message_handler(commands=['start'])
def send_welcome(message):
    bot_tb.send_message(message.chat.id,'Привет, я бот, я помогаю вам играть в Морской бой')
    d=base.get_datawait()
    if d is None:
        bot_tb.send_message(message.chat.id, 'Ждем второго игрока')
        data=base.Add_user(message)
        base.Greate_room('wait',data)
    else:
        bot_tb.send_message(message.chat.id, 'Игрок найден')
        s=base.add_user_in_room(message)
        game=Play()
        game.generate_position()
        name_file=game.save_file()
        base.save_file(name_file, s.user1, s.id)
        game.generate_position()
        name_file = game.save_file()
        base.save_file(name_file, s.user2, s.id)


@bot_tb.message_handler(content_types=["text"])
def send_welcome(message):
        number=message.text[0]
        data=base.file_room(message, number)
        if (data==-1):
            bot_tb.send_message(message.chat.id, 'Не Ваш ход')
        game = Play()
        answer=game.step_add(message.text.split('-')[1], data.name)
        if answer == 'мимо':
            base.change_flag(number,data.room_id)

        bot_tb.send_message(message.chat.id, answer)

bot_tb.infinity_polling(none_stop=True, interval=0.5)