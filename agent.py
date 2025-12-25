import telebot
import os
import subprocess

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'

@bot.message_handler(commands=['exec'])
def handle_exec(message):
    if str(message.chat.id) == CHAT_ID:
        cmd = message.text.replace('/exec ', '')
        try:
            # Выполнение любой команды PowerShell через Telegram
            result = subprocess.check_output(["powershell", "-Command", cmd], stderr=subprocess.STDOUT, shell=True)
            bot.reply_to(message, f"✅ Выполнено:\n{result.decode('cp1251')}")
        except Exception as e:
            bot.reply_to(message, f"❌ Ошибка: {e}")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "🛰️ Жду команду /exec для управления системой.")

if __name__ == '__main__':
    print("🛰️ v6.0 АВТОНОМИЯ: Система управления готова.")
    bot.polling(none_stop=True)