import json

#Функция загрузки данных
def load_heroes():
    try:
        with open("heroes.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что файл heroes.json существует.")
        return []

#Функция сохранения данных
def save_heroes(heroes):
    try:
        with open("heroes.json", "w") as file:
            json.dump(heroes, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")

#Функция вывода героев
def show_heroes(heroes):
    print("\n--- Герои ---")
    if not heroes:
        print("Нет героев в списке.")
    else:
        for hero in heroes:
            name = hero.get("name", "Неизвестный")
            level = hero.get("level", 0)
            power = hero.get("power", 0.0)
            print(f"{name}, уровень: {level}, сила: {power}")

#Функция добавления героя
def add_hero():
    print("\n ---Добавление нового героя---")
    try:
        name = input("Введите имя героя: ").strip()
        if not name:
            print("Имя не может быть пустым!")
            return
        level = int(input("Введите уровень героя (целое число): "))
        if level < 0:
            print("Уровень героя не может быть отрицательным")
            return
        power = float(input("Введите силу героя (дробное число): "))
        if power < 0:
            print("Сила героя не может быть отрицательным")
            return
        new_hero = {
            "name": name,
            "level": level,
            "power": power
        }
        heroes = load_heroes()
        for hero in heroes:
            if hero["name"].lower() == name.lower():
                print(f"Герой с именем {name} уже существует!")
                return
        heroes.append(new_hero)
        save_heroes(heroes)
        print(f"Герой '{name}' успешно добавлен!")
    except ValueError as e:
        print(f"Ошибка ввода данных {e}")
        print("Проверьте правильность ввода чисел")
    except Exception as e:
        print(f"Неожиданная ошибка {e}")

def remove_hero():
   name_to_remove = input("Какого героя удалить? ")

   heroes = load_heroes()
   updated_heroes = [h for h in heroes if h["name"] != name_to_remove]

   if len(updated_heroes) < len(heroes):
       save_heroes(updated_heroes)
       print("Герой удален!")
   else:
       print("Ошибка: такого героя нет.")
def main_menu():
   while True:
       print("\n=== База героев фэнтези ===")
       print("1 — Посмотреть всех героев")
       print("2 — Добавить героя")
       print("3 — Удалить героя")
       print("4 — Выход")
       print("5 — Битва с драконом")

       choice = input("Выберите действие: ")

       heroes = load_heroes()

       if choice == "1":
           show_heroes(heroes)
       elif choice == "2":
           add_hero()
       elif choice == "3":
           remove_hero()
       elif choice == "4":
           print("До встречи! Все изменения сохранены.")
           break
       elif choice == "5":
           battle_with_dragon(load_heroes())
       else:
           print("Неверный выбор. Попробуйте снова.")

def battle_with_dragon(heroes):
   name = input("Какой герой будет сражаться с драконом? ")

   found = False
   for hero in heroes:
       if hero["name"].lower() == name.lower():
           found = True
           if hero["power"] > 70:
               print(f"{hero['name']} победил дракона!")
           else:
               print(f"{hero['name']} проиграл. Дракон слишком силён.")

   if not found:
       print("Такого героя нет.")

main_menu()



