import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'
PATH = r"G:\My Drive\Программирование\Test3"

dishes = """1. Массаман карри (Таиланд)
2. Неаполитанская пицца (Италия)
3. Шоколад (Мексика)
4. Суши (Япония)
5. Пекинская утка (Китай)
6. Гамбургер (США)
7. Пельмени (Россия)
8. Паэлья (Испания)
9. Круассан (Франция)
10. Лазанья (Италия)"""

try:
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    with open(os.path.join(PATH, "Best_Dishes.txt"), "w", encoding="utf-8") as f:
        f.write(dishes)
    bot.send_message(CHAT_ID, "✅ Тест 3 ПРОЙДЕН: Папка Test3 и 10 блюд созданы на диске G!")
    print("✅ Файлы Теста 3 созданы успешно.")
except Exception as e:
    print(f"❌ Ошибка: {e}")