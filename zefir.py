import   telebot
# from lib import *
#from mail import *
import re
from telebot import types
import sched, time
# from scheduler import *
#from sheet import *
#from buttons import *
#from checker import *
bot = telebot.TeleBot('5223565829:AAEvNDBzb0C9dJokI3OLlk8tqMprj1G-c4Y');


main_menutab         = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
box_type         = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
marshmallow_type         = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
zefir_type         = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
marshmallow_tastetab   = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
zefir_1_2  = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
zefir_1_2_3 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
# zefir_tastetab = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
zefir_tastetab = telebot.types.InlineKeyboardMarkup(row_width=6)


Buy           = types.KeyboardButton(text='Зробити замовлення')
Registration           = types.KeyboardButton(text='Реєстрація')
Entrance           = types.KeyboardButton(text='Увійти')
Track           = types.KeyboardButton(text='Відслідкувати')

Marshmallow           = types.KeyboardButton(text='Маршмелоу')
Zefir           = types.KeyboardButton(text='Зефір')
Box_mix           = types.KeyboardButton(text='Бокс-мікс')

Marshmallow1           = types.KeyboardButton(text='Маршмелоу квадратні в прозорому пакуванні (5грншт)')
Marshmallow2           = types.KeyboardButton(text='Маршмелоу в коробці 16шт - 350г (100грн)')
Marshmallow3           = types.KeyboardButton(text='Маршмелоу-лапки 100г (50грн)')
Marshmallow4           = types.KeyboardButton(text='Маршмелоу ваніль 100г (30грн)')

Zefir1           = types.KeyboardButton(text='3шт - 45грн')
Zefir2           = types.KeyboardButton(text='9шт - 135грн')
Zefir3           = types.KeyboardButton(text='15шт - 225грн')

Marshmallow1           = types.KeyboardButton(text='банан-шоколад')
Marshmallow2           = types.KeyboardButton(text='вишня-шоколад')
Marshmallow3           = types.KeyboardButton(text='вишня-арахісова паста')
Marshmallow4           = types.KeyboardButton(text='чорниця-лаванда')
Marshmallow5           = types.KeyboardButton(text='мята-шоколад')
Marshmallow6           = types.KeyboardButton(text='ваніль-мигдаль')

Zefir_1  = types.KeyboardButton(text='1')
Zefir_2  = types.KeyboardButton(text='2')

Zefir__1 = types.KeyboardButton(text='1')
Zefir__2 = types.KeyboardButton(text='2')
Zefir__3 = types.KeyboardButton(text='3')

# zefir_tastetab1 = types.KeyboardButton(text='банан-шоколад')
zefir_tastetab1 = telebot.types.InlineKeyboardButton('яблуко', callback_data='яблуко')
zefir_tastetab2 = telebot.types.InlineKeyboardButton('полуниця', callback_data='полуниця')
zefir_tastetab3 = telebot.types.InlineKeyboardButton('смородина', callback_data='смородина')
zefir_tastetab4 = telebot.types.InlineKeyboardButton('банан', callback_data='банан')
zefir_tastetab5 = telebot.types.InlineKeyboardButton('вишня', callback_data='вишня')
zefir_tastetab6 = telebot.types.InlineKeyboardButton('лимон-кокос', callback_data='лимон-кокос')


main_menutab.add(Buy, Registration, Entrance, Track)
box_type.add(Marshmallow, Zefir, Box_mix)
marshmallow_type.add(Marshmallow1, Marshmallow2, Marshmallow3, Marshmallow4)
zefir_type.add(Zefir1, Zefir2, Zefir3)
marshmallow_tastetab.add(Marshmallow1, Marshmallow2, Marshmallow3, Marshmallow4, Marshmallow5, Marshmallow6)
zefir_1_2.add(Zefir_1, Zefir_2)
zefir_1_2_3.add(Zefir__1, Zefir__2, Zefir__3)
zefir_tastetab.add(zefir_tastetab1, zefir_tastetab2, zefir_tastetab3, zefir_tastetab4, zefir_tastetab5, zefir_tastetab6)

@bot.message_handler(commands=['start'])
def main_menu(message):
    bot.send_message(message.chat.id, "Привіт, обери наступну дію:", reply_markup=main_menutab)
    bot.register_next_step_handler(message, menu)


# def main_menu(message):
# 	bot.send_message(message.chat.id, "Привіт, обери наступну дію:", reply_markup=main_menu)
#     bot.register_next_step_handler(message, menu)

def menu(message):
    if message.text == 'Зробити замовлення':
        buy(message)
    if message.text == 'Реєстрація':
        registration(message)
    if message.text == 'Увійти':
        entrance(message)
    if message.text == 'Відслідкувати':
        tracking(message)

def buy(message):
    bot.send_message(message.chat.id, "Що бажаєш замовити?", reply_markup=box_type)
    bot.register_next_step_handler(message, box)

def box(message):
    if message.text == 'Маршмелоу':
        bot.send_message(message.chat.id, "Обери свою коробочку", reply_markup=marshmallow_type)
        bot.register_next_step_handler(message, marshmallow_taste)
    if message.text == 'Зефір':
        bot.send_message(message.chat.id, "Обери свою коробочку", reply_markup=zefir_type)
        bot.register_next_step_handler(message, zefir_qtaste)
    if message.text == 'Бокс-мікс':
        zefirbox_taste(message)

def marshmallow_taste(message):
    if message.text == 'Маршмелоу в коробці 16шт - 350г (100грн)' or 'Маршмелоу квадратні в прозорому пакуванні (5грншт)':
        bot.send_message(message.chat.id, "Обери смак", reply_markup=marshmallow_tastetab)
        bot.register_next_step_handler(message, presale)
    if message.text == 'Маршмелоу-лапки 100г (50грн)' or 'Маршмелоу ваніль 100г (30грн)':
        bot.register_next_step_handler(message, presale)

def zefir_qtaste(message):
    if message.text == '3шт - 45грн':
        bot.send_message(message.chat.id, "Обери смак", reply_markup=zefir_tastetab)
        bot.register_next_step_handler(message, presale)
    if message.text == '9шт - 135грн':
        bot.send_message(message.chat.id, "Обери кількість смаків", reply_markup=zefir_1_2)
        bot.register_next_step_handler(message, zefir_taste)
    if message.text == '15шт - 225грн':
        bot.send_message(message.chat.id, "Обери кількість смаків", reply_markup=zefir_1_2_3)
        bot.register_next_step_handler(message, zefir_taste)

@bot.callback_query_handler(func=lambda message: True)
# @bot.message_handler(content_types=["text"])
def zefir_taste(message):
    if message.text == '2':
        bot.send_message(message.chat.id, "Обери перший смак", reply_markup=zefir_tastetab)
        bot.register_next_step_handler(message, zefir_2taste)
    if message.text == '3':
        bot.send_message(message.chat.id, "Обери перший смак", reply_markup=zefir_tastetab)
        bot.register_next_step_handler(message, zefir_3_1taste)
    else:
        bot.send_message(message.chat.id, "Обери смак", reply_markup=zefir_tastetab)
        bot.register_next_step_handler(message, presale)

def zefir_2taste(message):
    bot.send_message(message.chat.id, "Обери другий смак", reply_markup=zefir_tastetab)
    bot.register_next_step_handler(message, presale)

def zefir_3_1taste(message):
    bot.send_message(message.chat.id, "Обери другий смак", reply_markup=zefir_tastetab)
    bot.register_next_step_handler(message, zefir_3_1taste)

def zefir_3_1taste(message):
    bot.send_message(message.chat.id, "Обери третій смак", reply_markup=zefir_tastetab)
    bot.register_next_step_handler(message, presale)


def presale(message):
    bot.send_message(message.chat.id, "дякую")
#def get_text_messages(message):
#    if message.text == "Привет":
#        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
#    elif message.text == "/help":
#        bot.send_message(message.from_user.id, "Напиши привет")
#    else:
#        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling()
