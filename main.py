from __future__ import annotations
import telebot
from telebot import types
from hf import classificate


# bot in Telegram @AITextRecognitionBot

def messagetoprompt(message: str):
    bot.send_message(message.from_user.id, "Обработка запроса...")
    classified = classificate(message.text)
    label = classified['label']
    score = classified['score']
    if label == 'human':
        label = 'человек'
    bot.reply_to(message, f'Текст сгенерировал {label} с вероятностью {round(score * 100, 2)}%')


bot = telebot.TeleBot('6737481601:AAEjCS6mF3hzdqxs3nMVPJYlRX1mxQrc-Gs')


@bot.message_handler(commands=['start'])  # стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Начать работу")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Здравствуйте", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    # Русский язык
    if message.text == 'Начать работу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Ввести текст')
        btn10 = types.KeyboardButton('🔙 Вернуться к началу')
        markup.add(btn1, btn10)
        bot.send_message(message.from_user.id,
                         "Это бот, созданный для помощи в распознавании текстовых работ, сгенерированных ИИ в рамках "
                         "исследовательского проекта",
                         reply_markup=markup)

    elif message.text == '🔙 Вернуться к началу':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Начать работу')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Здравствуйте", reply_markup=markup)

    elif message.text == 'Ввести текст':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("🔙 Главное меню")
        markup.add(btn11)
        bot.send_message(message.from_user.id,
                         'Введите текст, который необходимо проверить',
                         parse_mode='Markdown')

    elif message.text == '🔙 Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Начать работу')
        markup.add(btn1)
        bot.send_message(message.from_user.id, "Здравствуйте", reply_markup=markup)
    # Small talk
    else:
        messagetoprompt(message)


bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть
