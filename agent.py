import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
HISTORY_PATH = r"G:\My Drive\Программирование\full_history_final.txt"

def log_and_notify(text, log_text, chat_id):
    try:
        # Пишем в историю
        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n{log_text}")
        
        # Шлем уведомление (с обработкой ошибки, если чат не найден)
        if chat_id:
            bot.send_message(chat_id, f"🔔 Sfera.AI: {text}")
        return True
    except Exception as e:
        print(f"Запись в историю прошла, но уведомление не ушло: {e}")
        return False

@bot.message_handler(func=lambda m: True)
def handle_all(message):
    print(f"Получено сообщение от ID {message.chat.id}: {message.text}")
    bot.reply_to(message, f"Ваш ID: {message.chat.id}. Система v5.3 на связи!")

if __name__ == '__main__':
    # Пытаемся отправить уведомление (если ID верный)
    log_and_notify("Система v5.3 онлайн!", "181. ТЕСТИРОВАНИЕ: Исправлена ошибка уведомлений (Chat ID).", "842426027")
    print("🛰️ v5.3 запущена. Напиши боту в Telegram, чтобы он узнал твой ID!")
    bot.polling(none_stop=True)