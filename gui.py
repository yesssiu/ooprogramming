import tkinter as tk
from task_manager_app import TaskManagerApp

task_manager = TaskManagerApp()
task_manager.read_users_from_json("users.json")

root = tk.Tk()
root.title("Task Management System")
root.geometry("500x300")

label = tk.Label(root, text="Welcome to TM System!", font=('Arial', 20))
label.pack(padx=20, pady=10)
label = tk.Label(root, text="What would you like to do?")
label.pack(padx=20, pady=5)

login_frame = tk.Frame(root)
login_frame.pack()

def check_info():
    username = entry_username.get()  # Corrected this line
    password = entry_password.get()
    
    # Call the login method in the TaskManagerApp instance
    user = task_manager.login(username, password)
    
    if user:
        # Successfully logged in, continue with GUI setup
        task_manager._user = user
        logged_in = tk.Toplevel()
        logged_in.geometry("550x770")
        logged_in.title("Logged in to TM System")
            
        label_welcome = tk.Label(logged_in, text="You are now logged in to TM System", font=('Arial', 18))
        label_welcome.pack(padx=10, pady=10)
            
        #Fields for adding tasks
        label_new_task = tk.Label(logged_in, text="Fill in the information to add a new task:")
        label_new_task.pack(padx=10, pady=10)
            
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
        desc_entry = tk.Entry(task_frame)
        desc_entry.grid(row=2, column=1, padx=10, pady=5)
            
        btn_create_task = tk.Button(logged_in, text="Create")
        btn_create_task.pack()
            
        #Top buttons in a grid
        buttongridTop = tk.Frame(logged_in)
        buttongridTop.pack(padx=10, pady=10)
            
        #Functionality for buttons
        def update_text_output(output):
            text_output.delete('1.0', tk.END)  # Clear previous content
            text_output.insert(tk.END, output)
            
        def viewMyTasks():
            output = task_manager.view_tasks()
            update_text_output(output)
            
        def viewAllTasks():
            output = task_manager.view_all_tasks()
            update_text_output(output)
            
        def viewUsers():
            output = task_manager.view_users()
            update_text_output(output)
        
        def close_root_window():
            root.destroy()
            
        btn_view_tasks = tk.Button(buttongridTop, text="View your tasks", command=viewMyTasks)
        btn_view_tasks.grid(row=0, column=0)
        btn_view_all_tasks = tk.Button(buttongridTop, text="Vew all tasks", command=viewAllTasks)
        btn_view_all_tasks.grid(row=0, column=1)
        btn_view_users = tk.Button(buttongridTop, text="View users", command=viewUsers)
        btn_view_users.grid(row=0, column=2)
            
        #Textbox for prints
        outputField = tk.Frame(logged_in)
        outputField.pack(padx=10, pady=10)
            
        text_output = tk.Text(outputField)
        text_output.insert(tk.END, "Printit tulee tähän")
        text_output.pack(padx=20, pady=20)
            
        #Bottom buttons in a grid
        buttongridBottom = tk.Frame(logged_in)
        buttongridBottom.pack(side=tk.BOTTOM, padx=10, pady=10)
        
        
        btn_exit = tk.Button(buttongridBottom, text="Exit", command=exit)
        btn_exit.grid(row=0, column=1)
        btn_log_out = tk.Button(buttongridBottom, text="Log Out", command=close_root_window)
        btn_log_out.grid(row=0, column=2)

    #Login button with command to retrieve entry values
    btn_login2 = tk.Button(login_frame, text="Submit", command=check_info)
    btn_login2.pack()
    

def register():
    pass

def exiting():
    root.destroy()

# Create entry widgets
entryFrame = tk.Frame(login_frame)
entryFrame.pack(padx=10, pady=10)

label_username = tk.Label(entryFrame, text="Username")
label_username.grid(row=0, column=0)
entry_username = tk.Entry(entryFrame)
entry_username.grid(row=0, column=1)

label_password = tk.Label(entryFrame, text="Password")
label_password.grid(row=1, column=0)
entry_password = tk.Entry(entryFrame, show="*")  # To hide the password
entry_password.grid(row=1, column=1)

# Login button with command to retrieve entry values
btn_login2 = tk.Button(login_frame, text="Log in", command=check_info)
btn_login2.pack()

#Buttons for root window
tm_buttons = tk.Frame(root)
tm_buttons.pack(side=tk.BOTTOM, padx=10, pady=20)

btn_register = tk.Button(tm_buttons, text="Register")
btn_register.grid(row=0, column=1)
btn_exit = tk.Button(tm_buttons, text="Exit", command=exiting)
btn_exit.grid(row=0, column=2)


root.mainloop()

