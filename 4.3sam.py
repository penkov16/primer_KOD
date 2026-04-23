import tkinter as tk

window = tk.Tk()
window.title("Форма регистрации")
window.geometry("400x300")
window.config(bg="#2c3e50")

top_frame = tk.Frame(
    window,
    bg="#ecf0f1",
    relief="groove",
    bd=2
)
top_frame.pack(pady=20, padx=20, fill="both", expand=True)




window.mainloop()