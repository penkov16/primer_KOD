sentence = input("Введите фразу: ") #пользователь вводит фрузу
repeat_count = int(input("Введите количество повторений: ")) #количество повторений

if repeat_count <= 0:
   print("Ошибка: количество повторений должно быть неотрицательным и не равно 0.")
else:
    for i in range(repeat_count):
        print(sentence)


