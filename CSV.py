import csv

shopping_list = [["Название", "Цена"], ["Хлеб", "30"], ["Молоко", "50"]]

# with open("shopping_list.csv", "w", newline="") as file:
#    writer = csv.writer(file)
#    writer.writerows(shopping_list)


with open("shopping_list.csv", "r") as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)