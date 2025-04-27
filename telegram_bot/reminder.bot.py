import telebot
from telebot import types
import requests
import json

TOKEN = "7151635814:AAFf6wnLE6JzMU6nyK0X8pkMtJeQLyjNpzA"
bot = telebot.TeleBot(TOKEN)
API = '857ac1d10f3746518fd7b208382889f5'

user_favorites = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! 👋 Этот бот специально разработан для того, "
                          "\nчто бы вы могли посмотреть погоду в своем городе или в любом другом ✏️"
                          "\nвведите название города")
    show_main_menu(message.chat.id)


def show_main_menu(chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Добавить город в избранное')
    btn2 = types.KeyboardButton('Показать избранные города')
    btn3 = types.KeyboardButton('Вывести погоду избранных городов')
    btn4 = types.KeyboardButton('Удалить город из избранного')
    markup.row(btn1, btn2, btn3, btn4)
    bot.send_message(chat_id, 'Выберите действие:', reply_markup=markup)


@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    chat_id = message.chat.id
    text = message.text.strip()

    if text == 'Добавить город в избранное':
        msg = bot.send_message(chat_id, "Введите название города, который хотите добавить в избранное:", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, add_to_favorites)

    elif text == 'Показать избранные города':
        show_favorites(chat_id)

    elif text == 'Вывести погоду избранных городов':
        show_favorite_weather(chat_id)

    elif text == 'Удалить город из избранного':
        msg = bot.send_message(chat_id, "Введите название города, который хотите удалить из избранного.", reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(msg, remove_from_favorites)

    else:
        get_weather(message)

def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = res.json()
    if data.get('cod') == 200:
        temp = data["main"]["temp"]
        wind_speed = data["wind"]["speed"]
        weather_conditions = data["weather"][0]["description"]
        bot.reply_to(message, f'Сейчас погода: в {city} {temp}℃'
                            f'\nСкорость ветра: {wind_speed} м/с'
                            f'\nПогодные условия: {weather_conditions}')

    else:
        bot.reply_to(message, f'Такого города {city} нет!')

def add_to_favorites(message):
    city = message.text.strip().lower()
    user_id = message.chat.id

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}')
    if res.status_code != 200:
        bot.send_message(user_id, f'Город {city} не найден.')
        show_main_menu(user_id)
        return

    if user_id not in user_favorites:
        user_favorites[user_id] = []

    if city not in user_favorites[user_id]:
        user_favorites[user_id].append(city)
        bot.send_message(user_id, f'Город {city.capitalize()} добавлен в избранное!')
    else:
        bot.send_message(user_id, f'Город {city.capitalize()} уже есть в избранном!')

    show_main_menu(user_id)

def remove_from_favorites(message):
    city = message.text.strip().lower()
    user_id = message.chat.id

    if user_id in user_favorites and city in user_favorites[user_id]:
        user_favorites[user_id].remove(city)
        bot.send_message(user_id, f'Город {city.capitalize()} удален из избранного!')
    else:
        bot.send_message(user_id, f'Город {city.capitalize()} не найден в избранном.')

    show_main_menu(user_id)

def show_favorites(chat_id):
    if chat_id in user_favorites and user_favorites[chat_id]:
        cities = "\n".join([city.capitalize() for city in user_favorites[chat_id]])
        bot.send_message(chat_id, f"Ваши избранные города:\n{cities}")
    else:
        bot.send_message(chat_id, "У вас пока нет избранных городов.")
    show_main_menu(chat_id)

def show_favorite_weather(chat_id):
    if chat_id not in user_favorites or not user_favorites[chat_id]:
        bot.send_message(chat_id, "У вас пока нет избранных городов.")
        show_main_menu(chat_id)
        return

    for city in user_favorites[chat_id]:
        res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
        if res.status_code == 200:
            data = res.json()
            temp = data["main"]["temp"]
            wind_speed = data["wind"]["speed"]
            weather_conditions = data["weather"][0]["description"]
            bot.send_message(chat_id, f'Сейчас погода: в {city} {temp}℃'
                                       f'\nСкорость ветра: {wind_speed} м/с'
                                       f'\nПогодные условия: {weather_conditions}')
        else:
            bot.send_message(chat_id, f'Город {city} не найден.')

    show_main_menu(chat_id)

bot.polling()
