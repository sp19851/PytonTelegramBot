from config import API_TOKEN
import telebot

bot = telebot.TeleBot(token=API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = f'{message.from_user.first_name}, welcome to the Bot!'
    bot.send_message(message.chat.id, welcome_text)


bot.polling(none_stop=True)