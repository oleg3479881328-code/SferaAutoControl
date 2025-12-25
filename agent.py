import telebot
import os

# Твой токен Telegram
bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "🤖 Sfera.AI: Автономный режим активирован через GitHub Sync. Версия 4.0")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"📡 Система Sfera.AI приняла: {message.text}\nСтатус: Ожидание автономных команд.")

if __name__ == '__main__':
    print("Бот v4.0 запущен и готов к работе...")
    bot.polling(none_stop=True)