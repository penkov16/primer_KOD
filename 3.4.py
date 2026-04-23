import re
from collections import Counter

# Запрашиваем путь к файлу у пользователя
file_path = input("Введите путь к файлу: ")

try:
    # Открываем файл и считываем содержимое
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Преобразуем весь текст в нижний регистр и удаляем знаки препинания
    words = re.findall(r'\b\w+\b', text.lower())

    # Подсчет частот слов
    word_counts = Counter(words)

    # Получение списка 10 самых частых слов
    top_10_words = word_counts.most_common(10)

    print("\nТоп 10 слов:")
    for word, count in top_10_words:
        print(f'"{word}" — {count} раз')

except FileNotFoundError:
    print(f"Файл '{file_path}' не найден.")