# hero_journey_bug.py — программа с багами

name = input("Введите имя вашего героя: ")
health = int(input("Введите начальное здоровье: "))
artifacts = int(input("Сколько у вас артефактов? "))

print(f"\n{name} отправился в путь")
print("На пути встречен дракон!")
dragon_damage = 30

# Урон дракона
health -= dragon_damage
if health < 0:
    health = 0

# Проверка выживания
if health > 0:
    print(f"{name} выжил после дракона!")
    print(f"Осталось здоровья: {health}")
    # Использование зелья
    use_potion = input("Хотите использовать зелье здоровья? (да / нет): ").lower()

    if use_potion == "да":
        if artifacts > 0:
            artifacts -= 1
            health += 20
            print("Вы выпили зелье. Здоровье восстановлено на 20 пунктов.")
        else:
            print("У вас нет артифактов для зелья!")
    elif use_potion == "нет":
        print("Вы решили не использовать зелье.")
    else:
        print("Неверный ввод. Вы пропустили возможность использовать зелье")

else:
    print(f"{name} был побеждён...")

# Вывод итога
print(f"\nИмя героя: {name}")
print(f"Здоровье: {health}")
print(f"Осталось артефактов: {artifacts}")

# Специальный приз
if artifacts >= 3 and health > 0:
    print("Вы получаете бонус: щит защиты!")
elif health <= 0:
    print("Герой мертв - бонус не получен")
else:
    print("Для получения бонуса нужно 3 и более артефактов")
