import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734' # Твой подтвержденный ID
HISTORY_PATH = r"G:\My Drive\Программирование\full_history_final.txt"

def log_and_notify(text, log_text):
    try:
        with open(HISTORY_PATH, "a", encoding="utf-8") as f:
            f.write(f"\n{log_text}")
        bot.send_message(CHAT_ID, f"✅ Sfera.AI: {text}")
        print(f"Уведомление отправлено на {CHAT_ID}")
    except Exception as e:
        print(f"Ошибка связи: {e}")

@bot.message_handler(commands=['search'])
def search_placeholder(message):
    bot.reply_to(message, "🔎 Функция поиска активирована. Напиши название сериала, и я проверю обновления.")

if __name__ == '__main__':
    log_and_notify("Связь установлена! Теперь я могу присылать уведомления автономно.", "182. СВЯЗЬ: Chat ID обновлен на 1793274734. Уведомления работают.")
    print("🛰️ v5.4 запущена. Проверь Telegram!")
    bot.polling(none_stop=True)