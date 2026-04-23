import tkinter as tk


def show_info():
    hero_name = hero_entry.get()
    pet_name = pet_entry.get()
    pet_type_selected = pet_type.get()

    if hero_name and pet_name and pet_type_selected != "Выберите тип питомца":
        result_text = f"Герой: {hero_name},\n Питомец: {pet_name}, {pet_type_selected}"
        result_label.config(text=result_text, bg="green")
    else:
        error_message = "Ошибка: Заполните все поля.\n"
        if not hero_name:
            error_message +="- Введите имя героя\n"
        if not pet_name:
            error_message += "- Введите имя питомца\n"
        if pet_type_selected == "Выберите тип питомца":
            error_message += "- Выберите тип питомца"

        result_label.config(text=error_message, bg="red")


window = tk.Tk()
window.title("Герой и питомец")
window.geometry("400x300")

hero_label = tk.Label(
    window,
    text="Имя героя:",
    font=("Arial", 10, "bold"))
hero_label.pack(pady=(5, 2))

hero_entry = tk.Entry(
    window,
    width=30)
hero_entry.pack(pady=(0, 2))

pet_label = tk.Label(
    window,
    text="Имя питомца:",
    font=("Arial", 10, "bold"))
pet_label.pack(pady=(3, 2))

pet_entry = tk.Entry(
    window,
    width=30)
pet_entry.pack(pady=(0, 5))

result_label = tk.Label(
    window,
    text="",
    bg="blue",
    font=("Arial", 12, "bold"),
    width=25,
    height=5,
    fg="white")
result_label.pack(pady=(5, 0))

info_button = tk.Button(
    window,
    text="Показать информацию",
    command=show_info, bg="lightblue").pack(pady=(5, 0))

pet_type = tk.StringVar(value="Выберите тип питомца")
options = ["Кот", "Пёс", "Попугай", "Черепаха"]
pet_menu = tk.OptionMenu(
    window,
    pet_type,
    *options)
pet_menu.pack(pady=(5, 0))




window.mainloop()

