#задание 1
#Шаг 1: объявляю переменные
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
#Шаг 2: вывожу на экран результаты арифметических операций
print("Сумма: ", x + y)# сумма
print("Разность: ", x - y)# разность
print("Произведение: ", x * y)# произведение
print("Частное: ", x / y)# частное
print("Остаток от деления: ", x % y)# остаток
print("Возведение в степень: ", x ** y)# степень
#Шаг 3: проверка четности суммы
parity = (x + y) % 2 == 0
print("Сумма чётная?", parity)

#задание 2
#Шаг 1: объявляю переменные
hero_health = int(input("Введите здоровье героя: "))
damage = int(input("Введите урон монстра: "))
#Шаг 2: Вычисляю выжел ли герой
remaining = hero_health - damage
survived = remaining > 0
print("Оставшееся здоровье: ", remaining)
print("Герой выжил? ", survived)

#задание 3
#Шаг 1: объявляю переменные
fuel_tank = float(input("Введите объём топливного бака (л): "))
fuel_consumption = float(input("Введите расход топлива на 100 км (л): "))
distance = float(input("Введите расстояние до цели (км): "))
#Шаг 2: провожу расчет на достаточность топлива
fuel_required = (fuel_consumption / 100) * distance
has_enough = fuel_tank >= fuel_required
print("Требуется топлива для перелета: ", fuel_required)
print("Хватит топлива для перелета? ", has_enough)
#
# number_of_hours = int(input("Введите количество часов: "))
# hourly_rate = int(input("Введите ставку за час: "))
# print("Зарплата: ", number_of_hours*hourly_rate)

# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# average_score = float(input("Введите средний балл: "))
# is_excellent = input("Является ли отличником? (да/нет): ").lower() == 'да'
# print("Имя: ", name)
# print("Возраст: ", age)
# print("Средний балл: ", average_score)
# print("Отличница: ", is_excellent)
#
# age = 20
# has_license = True
# gpa = 4.5
# print("Возраст: ", age)
# print("Есть права: ", has_license)
# print("Средний балл: ", gpa)
#
# if age >= 18 and has_license:
#    print("Рекомендация: Можно устраиваться на работу")
# elif age >= 18 and not has_license:
#    print("Нужно получить водительские права")
# else:
#    print("Не достиг совершеннолетия")
#
# if gpa > 4:
#    print("Участвует в стажировке: Да")
# else:
#    print("Участвует в стажировке: Нет")