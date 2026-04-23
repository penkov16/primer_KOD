# шаг 1
import tkinter as tk
from tkinter import messagebox
import json


# шаг 2
def load_task():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# шаг 3
def save_task(task_list):
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(task_list, file, ensure_ascii=False, indent=4)


# шаг 7
def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)


# шаг 5
def add_task():
    task = entry_task.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        save_task(tasks)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Предупреждение", "Введите название")


# шаг 6
def remove_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
        save_task(tasks)
    else:
        messagebox.showwarning("Предупреждение", "Выберите продукт для удаления")


# шаг 4

window = tk.Tk()
window.title("Список продуктов")
window.geometry("400x400")
window.resizable(False, False)
window.configure(bg="#f5f5f5")

title_label = tk.Label(
    window,
    text="🥩 Мой список продуктов",
    font=("Arial", 14, "bold"),
    bg="#f5f5f5",
    fg="#2c3e50"
)
title_label.pack(pady=(15, 10))

task_listbox = tk.Listbox(
    window,
    height=10,
    width=50,
    font=("Arial", 11),
    bg="#ffffff",
    fg="#333333",
    selectbackground="#4caf50",
    selectforeground="white",
    relief="solid",
    bd=1
)
task_listbox.pack(pady=(5, 15), padx=20)

entry_task = tk.Entry(
    window,
    width=40,
    font=("Arial", 12),
    relief="sunken",
    bd=2
)
entry_task.pack(pady=(5,15), padx=20)

add_button = tk.Button(
    window,
    text="➕ Добавить продукт",
    font=("Arial", 10, "bold"),
    fg="white",
    bd=2,
    bg="#4CAF50",
    cursor="hand2",
    command=add_task,
    relief="raised",
    pady=5,
    padx=10
)
add_button.pack(pady=(0,10))

remove_button = tk.Button(
    window,
    text="🗑 Удалить продукт",
    font=("Arial", 10, "bold"),
    bg="#e74c3c",
    fg="white",
    activebackground="#c0392b",
    activeforeground="white",
    cursor="hand2",
    command=remove_task,
    relief="raised",
    bd=2,
    padx=10,
    pady=5
)
remove_button.pack(pady=(0, 20))

tasks = load_task()
update_listbox()

window.mainloop()