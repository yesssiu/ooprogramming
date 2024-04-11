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
            logged_in.geometry("450x450")
            logged_in.title("Logged in to TM System")
            
            label_welcome = tk.Label(logged_in, text="You are now logged in to TM System")
            label_welcome.pack(padx=10, pady=10)
            
            #Top buttons in a grid
            buttongridTop = tk.Frame(logged_in)
            buttongridTop.pack(padx=10, pady=10)
            
            btn_view_tasks = tk.Button(buttongridTop, text="View your tasks")
            btn_view_tasks.grid(row=0, column=0)
        
            btn_view_all_tasks = tk.Button(buttongridTop, text="Vew all tasks")
            btn_view_all_tasks.grid(row=0, column=1)
            
            btn_view_users = tk.Button(buttongridTop, text="View users")
            btn_view_users.grid(row=0, column=2)
            
            #Fields for adding tasks
            task_frame = tk.Frame(logged_in)
            task_frame.pack(padx=10, pady=5)
            
            name_label = tk.Label(task_frame, text='Name')
            name_label.grid(row=0, column=0, padx=10, pady=5)
            
            name_entry = tk.Entry(task_frame)
            name_entry.grid(row=0, column=1, padx=10, pady=5)
            
            category_label = tk.Label(task_frame, text='Category')
            category_label.grid(row=1, column=0, padx=10, pady=5)
            
            category_entry = tk.Entry(task_frame)
            category_entry.grid(row=1, column=1, padx=10, pady=5)
            
            desc_label = tk.Label(task_frame, text='Description')
            desc_label.grid(row=2, column=0, padx=10, pady=5)
            
            add_task_desc = tk.Entry(task_frame)
            add_task_desc.grid(row=2, column=1, padx=10, pady=5)
            
            #Bottom buttons in a grid
            buttongridBottom = tk.Frame(logged_in)
            buttongridBottom.pack(padx=10, pady=10)
            
            btn_exit = tk.Button(buttongridBottom, text="Exit", command=exit)
            btn_exit.grid(row=0, column=1)
            
            btn_log_out = tk.Button(buttongridBottom, text="Log Out", command=logged_in.destroy)
            btn_log_out.grid(row=0, column=2)

            
    #Login button with command to retrieve entry values
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

