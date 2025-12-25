import telebot
import os

bot = telebot.TeleBot('8559453371:AAGZVieHWP7htcNPivy0Lm5us_idQOaTADc')
CHAT_ID = '1793274734'
DIR_PATH = r"G:\My Drive\Программирование\Test1"
FILE_PATH = os.path.join(DIR_PATH, "Borsch_Recipes.txt")

recipes = "1. Классический\n2. С пампушками\n3. Полтавский\n4. Постный\n5. Сибирский\n6. С копченостями\n7. Зеленый\n8. На ребрышках\n9. Гетманский\n10. Холодный"

try:
    if not os.path.exists(DIR_PATH):
        os.makedirs(DIR_PATH)
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        f.write(recipes)
    bot.send_message(CHAT_ID, "🚀 ПРИНУДИТЕЛЬНЫЙ ТЕСТ: Папка Test1 и файл созданы успешно!")
    print("✅ Тест пройден. Файл на диске G: обновлен.")
except Exception as e:
    print(f"❌ Ошибка теста: {e}")