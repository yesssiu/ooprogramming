import tkinter as tk

root = tk.Tk()
def exiting():
    root.destroy()
login_frame = tk.Frame(root)
login_frame.pack()

def login():
    # Clear any existing entry widgets
    for widget in login_frame.winfo_children():
        widget.destroy()

    # Create entry widgets
    entry_username = tk.Entry(login_frame)
    entry_username.pack()

    entry_password = tk.Entry(login_frame, show="*")  # To hide the password
    entry_password.pack()
    def check_info():
        username = entry_username.get()
        password = entry_password.get()
        if username == "asd" and password == "asd":
            logged_in = tk.Toplevel()
            logged_in.geometry("400x400")
            logged_in.title("Logged in to TM System")
            label_welcome = tk.Label(logged_in,text="You are now logged in to TM System")
            label_welcome.pack()
            btn_view_tasks = tk.Button(logged_in,text="Own tasks")
            btn_view_tasks.pack(side="left",anchor="n")
            btn_view_all_tasks = tk.Button(logged_in, text="All tasks")
            btn_view_all_tasks.pack(side="left",anchor="n")
            btn_add_task = tk.Button(logged_in,text="Add Task")
            btn_add_task.pack(side="left",anchor="n")
            btn_view_users = tk.Button(logged_in,text="View users")
            btn_view_users.pack(side="left",anchor="n")
            btn_exit = tk.Button(logged_in,text="Exit", command=exit)
            btn_exit.pack(side="right",anchor="n")
            btn_log_out = tk.Button(logged_in,text="Log Out", command=logged_in.destroy)
            btn_log_out.pack(side="right",anchor="n")

    # Login button with command to retrieve entry values
    btn_login2 = tk.Button(login_frame, text="Log in", command=check_info)
    btn_login2.pack()

root.title("Task Management System")
root.geometry("500x500")
label = tk.Label(root, text="Welcome to TM System!\n What you want to do?")
label.pack()
btn_login = tk.Button(root, text="Log in", command=login)
btn_login.pack()
btn_register = tk.Button(root, text="Register")
btn_register.pack()
btn_exit = tk.Button(root, text="Exit", command=exiting)
btn_exit.pack()
root.mainloop()