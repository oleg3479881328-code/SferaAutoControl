import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'
PATH = r"G:\My Drive\Программирование\Test6"

discoveries = """1. Огонь — основа цивилизации.
2. Колесо — революция в транспорте.
3. Печатный станок — доступ к знаниям.
4. Паровой двигатель — промышленная революция.
5. Электричество — новая эра энергии.
6. Пенициллин — победа над инфекциями.
7. Полупроводники — рождение электроники.
8. Интернет — глобальная сеть.
9. Генная инженерия (CRISPR) — управление кодом жизни.
10. Искусственный интеллект — новая ступень эволюции."""

def run_test_6():
    try:
        if not os.path.exists(PATH):
            os.makedirs(PATH)
        with open(os.path.join(PATH, "Discoveries.txt"), "w", encoding="utf-8") as f:
            f.write(discoveries)
        bot.send_message(CHAT_ID, "✅ ТЕСТ 6 ВЫПОЛНЕН: 10 открытий записаны на диск G!")
        print("✅ Тест 6: Папка и файл созданы.")
    except Exception as e:
        print(f"❌ Ошибка в Тесте 6: {e}")

if __name__ == '__main__':
    run_test_6()
    bot.polling(none_stop=True)