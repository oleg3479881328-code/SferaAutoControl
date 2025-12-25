import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'
BASE_DIR = r"G:\My Drive\Программирование"
TEST_DIR = os.path.join(BASE_DIR, "Test")

series_list = """1. Игра престолов (2011)
2. Во все тяжкие (2008)
3. Очень странные дела (2016)
4. Ходячие мертвецы (2010)
5. Игра в кальмара (2021)
6. Разделение (2022)
7. Остаться в живых (2004-2010)
8. Йеллоустоун (2018)
9. Черное зеркало (2011)
10. Андор (2022)"""

def execute_task():
    try:
        # Создаем папку
        if not os.path.exists(TEST_DIR):
            os.makedirs(TEST_DIR)
        
        # Создаем файл
        file_path = os.path.join(TEST_DIR, "Popular_Series.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(series_list)
        
        # Уведомляем
        bot.send_message(CHAT_ID, "✅ Папка 'Test' создана, список сериалов сохранен на диске G!")
        print("Задача выполнена успешно.")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    execute_task()
    bot.polling(none_stop=True)