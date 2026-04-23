import tkinter as tk

mouse_click = 0
space_click = 0
total_events = 0


def update():
    mouse_label.config(text=f"Кликов мышью: {mouse_click}")
    space_label.config(text=f"Нажатий пробела: {space_click}")
    total_label.config(text=f"Всего событий: {total_events}")


def on_moise_click(event):
    global mouse_click, total_events
    mouse_click += 1
    total_events += 1
    update()


def on_space_click(event):
    global space_click, total_events
    space_click += 1
    total_events += 1
    update()


def reset():
    global mouse_click, total_events, space_click
    mouse_click = 0
    space_click = 0
    total_events = 0
    update()


window = tk.Tk()
window.title("Счетчик событий")
window.geometry("300x200")

mouse_label = tk.Label(
    window,
    text="Кликов мышью: 0",
    font=("Arial", 12)
)
mouse_label.pack(pady=(25, 0))

space_label = tk.Label(
    window,
    text="Нажатий пробела: 0",
    font=("Arial", 12)
)
space_label.pack(pady=(20, 0))

total_label = tk.Label(
    window,
    text="Всего событий: 0",
    font=("Arial", 14, "bold")
)
total_label.pack(pady=(20, 0))

reset_button = tk.Button(
    window,
    text="Сбросить",
    command=reset
)
reset_button.pack(pady=10)

window.bind("<Button-1>", on_moise_click)
window.bind("<space>", on_space_click)

window.mainloop()
