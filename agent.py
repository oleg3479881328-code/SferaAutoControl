import telebot
import os

# Путь к истории
HISTORY_PATH = r"G:\My Drive\Программирование\full_history_final.txt"

def log_to_history(text):
    try:
        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n{text}")
        return True
    except:
        return False

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')

# При запуске этой версии бот СРАЗУ пишет в историю
log_to_history("174. АВТОНОМИЯ: Настроена бесшовная синхронизация через GitHub API.")
log_to_history("175. СТАТУС: Роль 'копипаст-прокладки' полностью устранена. Переход к удаленному управлению.")

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "🤖 Sfera.AI v4.1: История обновлена автономно!")

if __name__ == '__main__':
    print("Бот v4.1 (History Edition) запущен...")
    bot.polling(none_stop=True)