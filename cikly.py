# #Задание №1
# secret_number = 7
#
# guess = None
# while guess != secret_number:
#     guess = int(input("Угадайте число от 1 до 10: "))
#     if guess < secret_number:
#         print("Мало!")
#     elif guess > secret_number:
#         print("Много!")
# print("Поздравляем! Вы угадали!")
#
# #Задание №2
# while True:
#     print("=== Калькулятор ===")
#     print("Пункты меню:")
#     print("1 - Сложить два числа")
#     print("2 - Вычесть два числа")
#     print("3 - Умножить два числа")
#     print("4 - Поделить два числа")
#     print("5 - Выйти из программы")
#
#     choice = int(input("Выберите действие (1-5): "))
#     if choice == 5:
#         print("До свидания!")
#         break
#
#     if choice not in [1, 2, 3, 4]:
#         print("Некорректный ввод.")
#         continue
#     number1 = float(input("Введите первое число: "))
#     number2 = float(input("Введите второе число: "))
#     if choice == 4:
#         if(number2 == 0):
#             print("Ошибка: деление на ноль невозможно")
#         else:
#             print(f"Ответ: {number1 / number2}")
#     elif choice == 3:
#         print(f"Ответ: {number1 * number2}")
#     elif choice == 2:
#         print(f"Ответ: {number1 - number2}")
#     elif choice == 1:
#         print(f"Ответ: {number1 + number2}")

sentence = input()