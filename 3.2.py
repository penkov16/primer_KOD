#Шаг 1
import random
from datetime import datetime
from collections import Counter

while True:
    print("\n Выберите команду: ")
    print("1. Бросить кости")
    print("2. Показать статистику")
    print("3. Выход.\n")
    guess = int(input("Ваша команда: "))
    if guess == 1:
        start_time = datetime.now()
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)
        print(f"Вы бросили кости: {number1} + {number2} = {number1+number2}")
        with open("dice_rolls.txt", "a", encoding="utf-8") as file:
            file.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ")
            file.write(f"Бросок: {number1} + {number2} = {number1+number2}\n")
        print("Результат записан в файл.")

    elif guess == 2:

        statistics = Counter()
        with open('dice_rolls.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # Извлекаем сумму из строки (число после последнего '=')
                try:
                    total = int(line.split('=')[1].strip())
                    statistics[total] += 1
                except (IndexError, ValueError):
                    continue  # Пропускаем некорректные строки

        print("\n Статистика бросков:")
        # Выводим суммы от 2 до 12 (возможные суммы при броске двух костей)
        for total in range(2, 13):
            count = statistics.get(total, 0)
            if count > 0:
                # Используем правильные окончания для слова "раз"
                word = "раз" if count == 1 else "раза"
                print(f"{total} — {count} {word}")

    elif guess == 3:
        print("До свидания!")
        break
    else:
        print("Некорректный ввод")















#         elapsed = (datetime.now() - start_time).seconds
#         if elapsed >= 60:
#             print(f"Время вышло! Загаданное число было: {secret_number}")
#             break
#
#     except ValueError:
#         print("Ошибка: введите целое число.")
#
# # Шаг 6
# end_time = datetime.now()
# elapsed_seconds = (end_time - start_time).seconds
#
# print(f"\n ⏰Конец игры: {end_time.strftime('%H:%M:%S')}")
# print(f"⏱️Вы потратили: {elapsed_seconds} секунд")
# print(f"🔢Число попыток: {attemps}")
#
# #Шаг 7
# with open("game_result.txt", "w", encoding="utf-8") as file:
#     file.write("Результаты игры 'Угадай число'\n")
#     file.write(f"Дата: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
#     file.write(f"Загаданное число: {secret_number}\n")
#     file.write(f"Число попыток: {attemps}\n")
#     file.write(f"Затраченное время: {elapsed_seconds} секунд\n")
#
#     if game_won:
#         file.write("Статус: Победа\n")
#     else:
#         file.write("Статус: Поражение\n")
#
# print("\n ✅ Результат сохранен в файл game_result.txt")






