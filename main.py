import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # توكن البوت من المتغير البيئي
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا بك! أنا بوت تيليجرام بسيط 🎉")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print("Bot is running...")
bot.infinity_polling()
