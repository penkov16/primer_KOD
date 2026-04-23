import tkinter as tk

window = tk.Tk()
window.title("Калькулятор калорий")
window.geometry("400x300")
window.resizable(False, False)
window.configure(bg="#ffffff")

#создание Frame
imput_frame = tk.Frame(
    window,
    width=380,
    height=150,
    bg="#f0f0f0",
    bd = 2,
    relief="groove"
)
imput_frame.place(x=10, y=10)

result_frame = tk.Frame(
    width=380,
    height=100,
    bg="#eaeaea"
)
result_frame.place(x=10, y=170)

#Виджеты во Frame
tk.Label(
    imput_frame,
    text="Ваш вес (кг):",
    bg="#f0f0f0"
).place(x=10, y=10)
weight_entry = tk.Entry(imput_frame, width=10)
weight_entry.place(x=130, y=10)

tk.Label(
    imput_frame,
    text="Рост (см):"
).place(x=10, y=40)
height_entry = tk.Entry(imput_frame, width=10)
height_entry.place(x=130, y=40)

tk.Label(imput_frame, text="Количество порций:").place(x=10, y=70)
portions_entry = tk.Entry(imput_frame, width=10)
portions_entry.place(x=130, y=70)

#Функция для расчета калорий
def calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        portions = int(portions_entry.get())
        bmr = 10*weight+6.25*height-5*25+5
        calories = bmr*0.8*portions
        result_label.config(text=f"Оценка калорий: {round(calories)} ккал")

    except ValueError:
        result_label.config(text="Ошибка: введите числа!")
        result_frame.config(bg="#ff0000")
tk.Button(imput_frame,
          text="Рассчитать",
          command=calculate,
          bg="#4caf50",
          fg="white").place(x=10, y=100)

#Вывод результата
result_label = tk.Label(result_frame, text="", font=("Arial", 14), bg="#eaeaea")
result_label.place(x=10,y=20)




window.mainloop()