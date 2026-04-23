import random


def game(number, secret_number):
    if number > secret_number:
        print("Слишком много")
        return False
    elif number < secret_number:
        print("Слишком мало")
        return False
    else:
        print("Угадал!")
        return True


def main():
    secret_number = random.randint(1, 10)
    print("Угадай число от 1 до 10")
    print("У тебя 5 попыток")
    i = 0
    while True:
        number = int(input("Введите число: "))
        first = game(number, secret_number)
        i += 1
        if first:
            print("Количество попыток: ", i)
            break
        if i > 4:
            print("Попытки закончились")
            break


if __name__ == "__main__":
    main()
