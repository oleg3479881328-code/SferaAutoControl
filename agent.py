import telebot
import os
import subprocess

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'

@bot.message_handler(func=lambda m: True)
def auto_exec(message):
    # Если я присылаю команду, начинающуюся с CMD:
    if message.text.startswith("CMD:"):
        cmd = message.text.replace("CMD:", "").strip()
        try:
            # Выполняем команду PowerShell напрямую
            output = subprocess.check_output(["powershell", "-Command", cmd], stderr=subprocess.STDOUT, shell=True)
            bot.send_message(CHAT_ID, f"✅ Исполнено:\n{output.decode('cp1251')}")
        except Exception as e:
            bot.send_message(CHAT_ID, f"❌ Ошибка исполнения: {e}")

if __name__ == '__main__':
    print("🚀 СИСТЕМА ПЕРЕВЕДЕНА В АВТОНОМНЫЙ РЕЖИМ v7.0")
    print("Теперь Gemini может управлять этим ПК через Telegram.")
    bot.polling(none_stop=True)