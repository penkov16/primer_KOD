# Программа управления фильмами
movies = []


def add_movie():
    name = input("Введите название фильма: ")
    if name == "":
        print("Название не может быть пустым!")
        return
    for movie in movies:
        if movie["name"].lower() == name.lower():
            print("Фильм с таким название уже добавлен")
            return

    genre = input("Введите жанр фильма: ").strip()
    if genre == "":
        print("Жанр не божет быть пустым!")
        return
    try:
        rating = float(input("Введите рейтинг фильма (от 0 до 10): "))
        if rating > 10 or rating < 0:
            print("Рейтинг должен быть от 0 до 10!")
            return
    except ValueError:
        print("Ошибка! Рейтинг должен быть числом!")

    movie = {"name": name, "genre": genre, "rating": rating}
    movies.append(movie)
    print(f"Фильм {name} добавлен")


def show_all_movies():
    if len(movies) == 0:
        print("Список фильмов пуст.")
        return
    else:
        for i in range(len(movies)):
            print(f"{i + 1}. {movies[i]["name"]} ({movies[i]["genre"]}) - Рейтинг: {movies[i]["rating"]}")
    print(f"Всего фильмов: {len(movies)}")


def find_movie():
    search = input("Введите название фильма для поиска: ").lower()
    found = False
    for movie in movies:
        if movie["name"].lower() == search:
            print("Найден фильм:")
            print("Название: " + movie["name"])
            print("Жанр: " + movie["genre"])
            print("Рейтинг: " + movie["rating"])
            found = True
    if not found:
        print("Фильм не найден.")


def sort_by_rating():
    sorted_movies = sorted(movies, key=lambda x: x["рейтинг"], reverse=True)
    for movie in sorted_movies:
        print(f"{movie['name']} - {movie['рейтинг']}")


def save_to_file():
    if len(movies) == 0:
        print("Список фильмов пуст. Сохранять нечего")
        return
    try:
        with open("movies.txt", "w") as f:
            for movie in movies:
                f.write(f"{movie["name"], movie["genre"], movie["rating"]} \n")
        print("Данные сохранены в файл.")
    except:
        print("Ошибка при сохранении")


def load_from_file():
    try:
        with open("movies.txt", "r") as f:
            for line in f.readlines():
                name, genre, rating = line.strip().split(",")
                movies.append({"name": name, "genre": genre, "rating": rating})
        print("Данные загружены из файла.")
    except FileNotFoundError:
        print("Файл не найден, начато заполнение с нуля.")


def main():
    print("Меню:")
    print("1. Добавить фильм")
    print("2. Показать все фильмы")
    print("3. Поиск фильма")
    print("4. Отсортировать по рейтингу")
    print("5. Сохранить в файл")
    print("6. Выход")

    while True:
        choice = input("Выберите действие: ")

        if choice == "1":
            add_movie()
            print()
        elif choice == "2":
            show_all_movies()
            print()
        elif choice == "3":
            find_movie()
            print()
        elif choice == "4":
            sort_by_rating()
            print()
        elif choice == "5":
            save_to_file()
            print()
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")


load_from_file()
main()
