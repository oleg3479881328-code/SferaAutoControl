import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '842426027' # Твой ID
HISTORY_PATH = r"G:\My Drive\Программирование\full_history_final.txt"

def log_and_notify(text, log_text):
    try:
        # Пишем в историю
        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n{log_text}")
        # Шлем уведомление
        bot.send_message(CHAT_ID, f"🔔 Sfera.AI: {text}")
        return True
    except Exception as e:
        print(f"Ошибка: {e}")
        return False

@bot.message_handler(commands=['info'])
def info(message):
    bot.reply_to(message, "🚀 v5.2 активна. Жду список сериалов для мониторинга.")

if __name__ == '__main__':
    log_and_notify("Система онлайн! Уведомления и история синхронизированы.", "180. УВЕДОМЛЕНИЯ: Настроен канал прямой связи через Telegram Bot API.")
    print("🛰️ v5.2 запущена. Проверь Telegram и файл истории...")
    bot.polling(none_stop=True)