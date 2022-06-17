import telebot
from utils import config

bot = telebot.TeleBot(config.BOT_TOKEN, parse_mode='MARKDOWN')

@bot.message_handler(commands=['hi'])
def send_welcome(message):
    bot.reply_to(message, "Hi! This chat id is `" + str(message.chat.id) + "`")

if __name__ == "__main__":
    bot.infinity_polling()

