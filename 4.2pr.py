import tkinter as tk
import os

window = tk.Tk()
window.title("Кликер")
window.geometry("300x250")


def load_record():
    if os.path.exists("record.txt"):
        with open("record.txt", "r") as file:
            try:
                return int(file.read())
            except ValueError:
                return 0
    return 0


score = 0  # Текущий счет
record = load_record()  # Рекорд из файла

label_score = tk.Label(
    window,
    text=f"Очки: {score}",
    font=("Arial", 14)
)
label_score.pack(pady=20)

label_record = tk.Label(
    window,
    text=f"Рекорд: {record}",
    font=("Arial", 12),
    fg="blue"
)
label_record.pack(pady=5)


def update_score():
    global score, record
    score += 1
    label_score.config(text=f"Очки: {score}")
    if score > record:
        record = score
        label_record.config(text=f"Рекорд: {record}")
        save_record()


def save_record():
    with open("record.txt", "w") as file:
        file.write(str(record))
        print(f"Рекорд {record} сохранен в файл")


click_button = tk.Button(
    window,
    text="Кликни меня!",
    width=20,
    height=2,
    command=update_score
)
click_button.pack(pady=20)


def key_event(event):
    if event.keysym in ["Return", "space"]:
        update_score()


window.bind("<Key>", key_event)


def reset_score():
    global score
    score = 0
    label_score.config(text=f"Очки: {score}")
    print("Счет сброшен")

reset_button = tk.Button(
    window,
    width=15,
    height=1,
    command=reset_score,
    text="Сбросить счет"
)
reset_button.pack(pady=5)

def on_closing():
    save_record()
    print("Приложение закрыто")
    window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)


window.mainloop()
