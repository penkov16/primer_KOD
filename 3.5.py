def load_notes():
    try:
        with open("notes.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(note + "\n")

def show_notes(notes):
    if not notes:
        print("Нет заметок")
    else:
        print("Список заметок:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

def add_notes(notes):
    note = input("Введите текст заметки: ")
    notes.append(note)
    print("Заметка добавлена!")

def delete_notes(notes):
    show_notes(notes)
    try:
        index = int(input("Введите номер заметки для удаления: ")) - 1
        if 0 <= index < len(notes):
            removed = notes.pop(index)
            print(f"Заметка {removed} удалена")
        else:
            print("Неверный номер заметки")
    except ValueError:
        print("Ошибка: введите число")


def main():
    notes = load_notes()

    while True:
        print("\nВыберите команду: ")
        print("1 - Посмотреть заметки")
        print("2 - Добавить заметку")
        print("3 - Удалить заметку")
        print("4 - Сохранить и выйти")

        choice = input("Введите номер: ")

        if choice == "1":
            show_notes(notes)
        elif choice == "2":
            add_notes(notes)
        elif choice == "3":
            delete_notes(notes)
        elif choice == "4":
            save_notes(notes)
            print("Заметки сохранены. До встречи!")
            break
        else:
            print("Неизвестная команда")

if __name__ == "__main__":
    main()

