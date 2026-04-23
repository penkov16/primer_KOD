import random
from datetime import datetime
from collections import Counter


def roll_dice():
    """
    Имитирует бросок двух шестигранных костей.
    Возвращает кортеж (значение1, значение2, сумма)
    """
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2, die1 + die2


def save_roll_to_file(die1, die2, total):
    """
    Сохраняет результат броска в файл с датой и временем
    """
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('dice_rolls.txt', 'a', encoding='utf-8') as file:
        file.write(f'[{timestamp}] Бросок: {die1} + {die2} = {total}\n')


def load_statistics():
    """
    Загружает историю бросков из файла и подсчитывает статистику
    """
    statistics = Counter()

    try:
        with open('dice_rolls.txt', 'r', encoding='utf-8') as file:
            for line in file:
                # Извлекаем сумму из строки (число после последнего '=')
                try:
                    total = int(line.split('=')[1].strip())
                    statistics[total] += 1
                except (IndexError, ValueError):
                    continue  # Пропускаем некорректные строки
    except FileNotFoundError:
        # Файл ещё не создан - нет статистики
        pass

    return statistics


def print_statistics(statistics):
    """
    Выводит статистику бросков
    """
    if not statistics:
        print("\n📊 Статистика бросков:")
        print("Бросков пока нет. Сыграйте первую игру!")
        return

    print("\n📊 Статистика бросков:")
    # Выводим суммы от 2 до 12 (возможные суммы при броске двух костей)
    for total in range(2, 13):
        count = statistics.get(total, 0)
        if count > 0:
            # Используем правильные окончания для слова "раз"
            word = "раз" if count == 1 else "раза"
            print(f"{total} — {count} {word}")

    total_rolls = sum(statistics.values())
    word = "бросок" if total_rolls == 1 else "броска" if total_rolls in [2, 3, 4] else "бросков"
    print(f"\nВсего совершено: {total_rolls} {word}")


def print_menu():
    """
    Выводит меню программы
    """
    print("\n" + "=" * 40)
    print("🎲 ИМИТАЦИЯ БРОСКОВ КОСТЕЙ 🎲")
    print("=" * 40)
    print("Выберите команду:")
    print("1. 🎲 Бросить кости")
    print("2. 📊 Показать статистику")
    print("3. 🚪 Выход")
    print("=" * 40)


def main():
    """
    Основная функция программы
    """
    print("🎲 Добро пожаловать в симулятор бросков костей!")
    print("Программа имитирует бросок двух шестигранных костей.")

    while True:
        print_menu()

        try:
            choice = input("> ").strip()

            if choice == '1':
                # Бросок костей
                die1, die2, total = roll_dice()
                print(f"\n🎲 Вы бросили кости: {die1} + {die2} = {total}")

                # Сохраняем результат в файл
                save_roll_to_file(die1, die2, total)
                print("✅ Результат записан в файл dice_rolls.txt")

            elif choice == '2':
                # Показать статистику
                statistics = load_statistics()
                print_statistics(statistics)

            elif choice == '3':
                # Выход из программы
                print("\n👋 До свидания! Спасибо за игру!")
                break

            else:
                print("❌ Ошибка: выберите команду 1, 2 или 3.")

        except KeyboardInterrupt:
            print("\n\n👋 Программа прервана пользователем. До свидания!")
            break
        except Exception as e:
            print(f"❌ Произошла ошибка: {e}")
            print("Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()