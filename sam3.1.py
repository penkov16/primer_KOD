import json


def load_dictionary() :
    """Загружает словарь из файла dictionary.json"""
    try:
        with open("dictionary.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Файл dictionary.json не найден. Создан новый словарь.")
        return {}


def save_dictionary(dictionary):
    """Сохраняет словарь в файл dictionary.json"""
    try:
        with open("dictionary.json", "w", encoding="utf-8") as file:
            json.dump(dictionary, file, ensure_ascii=False, indent=4)
        return True
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
        return False


def add_word(dictionary):
    """Добавляет новое слово в словарь"""
    print("\n--- Добавление нового слова ---")

    english = input("Введите слово на английском: ").strip().lower()

    if not english:
        print("Слово не может быть пустым!")
        return dictionary

    # Проверяем, существует ли уже это слово
    # if english in dictionary:
    #     print(f"Слово '{english}' уже существует в словаре.")
    #     overwrite = input("Перезаписать перевод? (да/нет): ").strip().lower()
    #     if overwrite not in ['да', 'д', 'yes', 'y']:
    #         print("Операция отменена.")
    #         return dictionary

    russian = input("Введите перевод: ").strip()

    if not russian:
        print("Перевод не может быть пустым!")
        return dictionary

    dictionary[english] = russian
    print(f"Слово '{english} → {russian}' добавлено в словарь.")
    return dictionary


def find_translation(dictionary):
    """Находит перевод слова"""
    print("\n--- Поиск перевода ---")

    word = input("Введите слово для перевода: ").strip().lower()

    if not word:
        print("Слово не может быть пустым!")
        return

    if word in dictionary:
        print(f"Перевод: {dictionary[word]}")
    else:
        print(f"Слово '{word}' не найдено в словаре.")

        # # Предлагаем похожие слова (опционально)
        # similar = [w for w in dictionary.keys() if word in w or w in word]
        # if similar:
        #     print("Возможно, вы искали одно из этих слов:")
        #     for similar_word in similar[:5]:  # Показываем до 5 похожих слов
        #         print(f"  {similar_word} → {dictionary[similar_word]}")


def show_all_words(dictionary):
    """Показывает все слова в словаре"""
    print("\n--- Слова в словаре ---")

    if not dictionary:
        print("Словарь пуст.")
        return

    # # Сортируем слова по алфавиту для удобного просмотра
    # sorted_words = sorted(dictionary.items(), key=lambda x: x[0])

    for english, russian in dictionary:
        print(f"{english} → {russian}")

    print(f"\nВсего слов в словаре: {len(dictionary)}")


def main():
    """Основная функция программы"""
    print("=== Простой переводчик ===")
    print("Загружаю словарь...")

    # Загружаем словарь
    dictionary = load_dictionary()

    while True:
        print("\n" + "=" * 40)
        print("Выберите команду:")
        print("1. Добавить слово")
        print("2. Найти перевод")
        print("3. Показать все слова")
        print("4. Сохранить и выйти")

        choice = input("> ").strip()

        if choice == "1":
            dictionary = add_word(dictionary)

        elif choice == "2":
            find_translation(dictionary)

        elif choice == "3":
            show_all_words(dictionary)

        elif choice == "4":
            # Сохраняем словарь перед выходом
            if save_dictionary(dictionary):
                print("\nДанные сохранены. До свидания!")
            else:
                print("\nНе удалось сохранить данные. Проверьте права доступа к файлу.")
            break

        else:
            print("Неверная команда. Пожалуйста, выберите от 1 до 4.")


if __name__ == "__main__":
    # try:
        main()
    # except KeyboardInterrupt:
    #     print("\n\nПрограмма прервана пользователем.")
    # except Exception as e:
    #     print(f"\nПроизошла неожиданная ошибка: {e}")