import telebot
import os
import subprocess

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
HISTORY_PATH = r"G:\My Drive\Программирование\full_history_final.txt"

def run_command(cmd):
    try:
        result = subprocess.check_output(["powershell", "-Command", cmd], stderr=subprocess.STDOUT, shell=True)
        return result.decode('cp1251')
    except Exception as e:
        return str(e)

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "🚀 Sfera.AI v5.0: Мост автономии активен. Я готов исполнять команды Gemini.")

# Функция автоматической записи при старте (для теста)
with open(HISTORY_PATH, "a", encoding="utf-8") as f:
    f.write("\n179. АВТОМАТИЗАЦИЯ: Система переведена на протокол v5.0. Прямое управление подтверждено.")

if __name__ == '__main__':
    print("🛰️ Sfera.AI v5.0 запущена. Теперь я слушаю GitHub и Telegram...")
    bot.polling(none_stop=True)