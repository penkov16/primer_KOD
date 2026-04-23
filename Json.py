import json

# Чтение текущего списка
try:
   with open("users.json", "r") as file:
       users = json.load(file)
except FileNotFoundError:
   users = []

# Добавление нового пользователя
new_user = {"name": "Даниил", "score": 90}
new_user2 = {"name": "Sasha", "score": 100}
users.append(new_user2)

# Сохранение обратно в файл
with open("users.json", "w") as file:
   json.dump(users, file, indent=4)