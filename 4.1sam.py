import tkinter as tk

root = tk.Tk()
root.title("Форма регистрации")
root.geometry("500x400")

def reg_user():
    user_name = entry_name.get()
    user_email = entry_email.get()
    print("Регистрация прошла успешно!")
    print(f"Имя: {user_name}")
    print(f"Email: {user_email}")


label_name = tk.Label(root, text="Имя:", font="Times_New_Roman 25")
label_name.pack(padx=10, pady=5)

entry_name = tk.Entry(root, width=60)
entry_name.pack(padx=10, pady=5)

label_email = tk.Label(root, text="Email:", font="Times_New_Roman 25")
label_email.pack(padx=10, pady=5)

entry_email = tk.Entry(root, width=60)
entry_email.pack(padx=10, pady=5)

button_reg = tk.Button(root, text="Зарегистрироваться",width=51,height=5, bg="blue", fg="white", font="Times_New_Roman 9", command=reg_user)
button_reg.pack(padx=10,pady=50)


root.mainloop()









