while True:
    # Вывод информации о программе
    print("\n=== Математический калькулятор ===")
    print("1 — Вычислить сумму от 1 до N")
    print("2 — Вычислить факториал числа")
    print("3 — Выход")

    # Получение данных от пользователя
    choice = input("Выберите действие (1–3): ")
    # Обработка случаев
    if choice == "1":
        n = int(input("Введите число N: "))
        total = 0
        for i in range(1, n + 1):
            total += i
        print(f"Сумма от 1 до {n}: {total}")
    elif choice == "2":
        n = int(input("Введите число N: "))
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"Факториал числа {n}: {factorial}")
    elif choice == "3":
        print("До встречи!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")