import telebot
from telebot import types
import json
import requests
token = ""
bot = telebot.TeleBot(token)


response = requests.get('https://minfin.com.ua/api/currency/ratelist/?currency1=usd&currency2=uah&converter_type=midbank')
json_data = json.loads(response.text)
usd_a = json_data['data']['rates']['buy']['USD']
usd_a = float(usd_a)
eur_a = json_data['data']['rates']['buy']['EUR']
eur_a = float(eur_a)
gbp_a = json_data['data']['rates']['buy']['GBP']
gbp_a = float(gbp_a)







@bot.message_handler(commands=['start', 'help'], content_types=['text'])
def send_welcome(message):
    bot.send_message(message.from_user.id, "Here you can type currency", reply_markup=keyboard())

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
    btn1 = types.KeyboardButton('USD🇺🇸')
    btn2 = types.KeyboardButton('EUR🇪🇺')
    btn3 = types.KeyboardButton('GBP🇬🇧')
    markup.add(btn1, btn2, btn3)
    return markup

@bot.message_handler(content_types=['text'])
def anymsg(message):
    if message.text == 'USD🇺🇸':
        bot.register_next_step_handler(message, test1)
    if message.text == 'EUR🇪🇺':
        bot.register_next_step_handler(message, test2)
    if message.text == 'GBP🇬🇧':
        bot.register_next_step_handler(message, test3)
def test1(message):
    try:
        message.text = float(message.text)
        texto1 = f'{message.text/usd_a}'
        texto1 = float(texto1)
        usd_txt = round(texto1, 2)
        bot.reply_to(message, usd_txt)
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Try again")

def test2(message):
    try:
        message.text = float(message.text)
        texto2 = f'{message.text/eur_a}'
        texto2 = float(texto2)
        eur_txt = round(texto2, 2)
        bot.reply_to(message, eur_txt)
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Try again")

def test3(message):
    try:
        message.text = float(message.text)
        texto3 = f'{message.text/usd_a}'
        texto3 = float(texto3)
        gbp_txt = round(texto3, 2)
        bot.reply_to(message, gbp_txt)
    except ValueError:
        bot.reply_to(message, "Enter only numbers. Try again")




#def process_firstname_step(message)
        #msg = bot.send_message(message.chat.id, Введите фамилию)
        #bot.register_next_step_handler(msg, process_lastname_step)
        #bot.reply_to(message, 'oooops')

if __name__ == '__main__':
    bot.polling(none_stop=True)
