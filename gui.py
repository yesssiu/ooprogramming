import tkinter as tk

root = tk.Tk()
root.title("Task Management System")

label = tk.Label(root, text="Welcome to TM System! What you want to do?")
label.pack()

btn_login = tk.Button(root, text="Log in")
btn_login.pack()
btn_register = tk.Button(root, text="Register")
btn_register.pack()
btn_exit = tk.Button(root, text="Exit", padx=15)
btn_exit.pack()

root.mainloop()