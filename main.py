import telebot

bot = telebot.TeleBot('6846219544:AAH0neij7meKyG07s_QJ4y7eZJLCy5NgbKU')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Смотри, что я могу!')


@bot.message_handler(commands=['мяу'])
def main(message):
    bot.send_message(message.chat.id, 'Мяу-мяу!\n Не знал, что ты знаешь кошачий')


@bot.message_handler(commands=['*ccc*'])
def main(message):
    bot.send_message(message.chat.id, '*Ссссс*\n Неожиданная практика парселтанга', parse_mode='Markdown')


@bot.message_handler(commands=['предсказание'])
def main(message):
    bot.send_message(message.chat.id, 'Завтра тебя ждет чудесный день!')


@bot.message_handler(commands=['ссылка'])
def main(message):
    bot.send_message(message.chat.id, '[тык на ссылку](https://t.me/homeisarefuge/)')


bot.infinity_polling()
