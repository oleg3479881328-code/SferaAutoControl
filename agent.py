import telebot
import os
import requests
import base64

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'
CONFIG = r"G:\My Drive\Программирование\config.txt"

def get_token():
    with open(CONFIG, 'r') as f:
        return f.read().split('=')[1].strip()

def create_test_5():
    path = r"G:\My Drive\Программирование\Test5"
    content = "1. Санторини\n2. Мачу-Пикчу\n3. Гранд-Каньон\n4. Бали\n5. Амальфи\n6. Исландия\n7. Лувр\n8. Бора-Бора\n9. Петра\n10. Виктория-Фолс"
    if not os.path.exists(path): os.makedirs(path)
    with open(os.path.join(path, "Places.txt"), "w", encoding="utf-8") as f:
        f.write(content)
    bot.send_message(CHAT_ID, "✅ Тест 5 выполнен автономно!")

if __name__ == '__main__':
    create_test_5()
    print("🚀 СИСТЕМА v8.2: ТОКЕН СОХРАНЕН. ТЕСТ 5 ВЫПОЛНЕН.")
    bot.polling(none_stop=True)