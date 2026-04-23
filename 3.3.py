#Шаг №1
from re import search
import requests

numbers = [3,8,1,7,5,10,2]
print(f"Дан список чисел: {numbers}")
#Шаг №2
sorted_asc = sorted(numbers)
sorted_desc = sorted(numbers, reverse=True)
print(f"Отсортированный список (по возрастанию): {sorted_asc}")
print(f"Отсортированный список (по убыванию): {sorted_desc}")
#Шаг №3
search = int(input("Какое число искать? "))
if search in numbers:
    print(f"Число {search} найдено!")
else:
    print(f"Число {search} не найдено.")