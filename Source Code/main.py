import tkinter as tk
from tkinter import messagebox
from database import login_user, register_user, add_task, get_tasks, get_task_details
from database import edit_task as db_edit_task, delete_task as db_delete_task

# Define task_ids list
task_ids = []

def login():
    username = username_entry.get()
    password = password_entry.get()
    user = login_user(username, password)
    if user:
        print("Login successful!")
        show_task_frame(username)
        hide_login_register_frame()
        display_tasks(username)
    else:
        messagebox.showerror("Error", "Invalid username or password")

def register():
    username = username_entry.get()
    password = password_entry.get()
    if username and password:  # Make sure username and password are not empty
        register_user(username, password)
        messagebox.showinfo("Success", "Registration successful!")
    else:
        messagebox.showerror("Error", "Please enter a username and password")

def display_tasks(username):
    global task_ids  # Declare task_ids as global to access it
    tasks = get_tasks(username)
    task_listbox.delete(0, tk.END)  # Clear the listbox before adding new tasks
    task_ids.clear()  # Clear the task_ids list
    for task in tasks:
        task_ids.append(task[0])  # Append task ID to task_ids list
        task_listbox.insert(tk.END, task[2])  # Display task description in the listbox

def add_task_gui():
    description = task_entry.get()
    due_date = f"{due_date_day_var.get()} {due_date_month_var.get()} {due_date_year_var.get()}"
    priority = priority_var.get()
    notes = notes_entry.get()  # Get notes from entry field
    tags = tags_entry.get()  # Get tags from entry field
    if description:
        add_task(username_entry.get(), description, due_date, priority, notes, tags)  # Pass new fields to add_task function
        display_tasks(username_entry.get())
        task_entry.delete(0, tk.END)  # Clear the task entry field
        notes_entry.delete(0, tk.END)  # Clear the notes entry field
        tags_entry.delete(0, tk.END)  # Clear the tags entry field
        # Clear dropdown menus
        due_date_day_var.set("Day")
        due_date_month_var.set("Month")
        due_date_year_var.set("Year")
        priority_var.set("Priority")
    else:
        messagebox.showerror("Error", "Please enter a task description")

def show_task_frame(username):
    login_register_frame.pack_forget()
    task_frame.pack(fill=tk.BOTH, expand=True)

def hide_login_register_frame():
    login_register_frame.pack_forget()

def show_task_details(event):
        # Get the index of the selected task
        index = task_listbox.curselection()[0]
        task_id = task_ids[index]  # Assuming task_ids is a list containing the IDs of tasks
        
        # Retrieve the details of the selected task from the database
        task_details = get_task_details(task_id)  # You'll need to implement get_task_details function in database.py
        
        # Convert due date format (e.g., "25 03 2024" to "25/03/2024")
        due_date = task_details[3].replace(" ", "/")
        
        # Function to delete the task
        def delete_task_func():
            db_delete_task(task_id)  # Call the delete_task function from database module
            display_tasks(username_entry.get())  # Update the task list after deleting the task
            task_details_window.destroy()  # Close the task details window after deleting the task
    
    # Function to edit the task
        def edit_task_func():
            # Get the updated task details from entry fields
            updated_description = description_entry.get()
            updated_due_date = due_date_entry.get()
            updated_priority = priority_entry.get()
            updated_notes = notes_entry.get()
            updated_tags = tags_entry.get()
        
            # Call the edit_task function from database module to update the task
            db_edit_task(task_id, updated_description, updated_due_date, updated_priority, updated_notes, updated_tags)
            
            # Update the task list after editing the task
            display_tasks(username_entry.get())
            
            # Close the task details window after editing the task
            task_details_window.destroy()
            
        # Create and display a popup or new window with the task details
        task_details_window = tk.Toplevel(root)
        task_details_window.title("Task Details")
        
        # Display task details in the popup or new window
        # You can use labels, entry fields, or text widgets to display the task details
        
        # Example: Display task description
        description_label = tk.Label(task_details_window, text="Description:")
        description_label.grid(row=0, column=0)
        description_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[2]))
        description_entry.grid(row=0, column=1)
        
        # Example: Display due date
        due_date_label = tk.Label(task_details_window, text="Due Date:")
        due_date_label.grid(row=1, column=0)
        due_date_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=due_date))
        due_date_entry.grid(row=1, column=1)
        
        # Example: Display priority
        priority_label = tk.Label(task_details_window, text="Priority:")
        priority_label.grid(row=2, column=0)
        priority_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[4]))
        priority_entry.grid(row=2, column=1)
        
        # Example: Display notes
        notes_label = tk.Label(task_details_window, text="Notes:")
        notes_label.grid(row=3, column=0)
        notes_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[5]))
        notes_entry.grid(row=3, column=1)
        
        # Example: Display tags
        tags_label = tk.Label(task_details_window, text="Tags:")
        tags_label.grid(row=4, column=0)
        tags_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[6]))
        tags_entry.grid(row=4, column=1)
        
        # Add buttons to edit and delete the task in a new row
        edit_button = tk.Button(task_details_window, text="Edit Task", command=edit_task_func)
        edit_button.grid(row=5, column=0)
        
        delete_button = tk.Button(task_details_window, text="Delete Task", command=delete_task_func)
        delete_button.grid(row=5, column=1)

        
        # Example: Display priority
        priority_label = tk.Label(task_details_window, text="Priority:")
        priority_label.grid(row=2, column=0)
        priority_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[4]))
        priority_entry.grid(row=2, column=1)
        
        # Example: Display notes
        notes_label = tk.Label(task_details_window, text="Notes:")
        notes_label.grid(row=3, column=0)
        notes_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[5]))
        notes_entry.grid(row=3, column=1)
        
        # Example: Display tags
        tags_label = tk.Label(task_details_window, text="Tags:")
        tags_label.grid(row=4, column=0)
        tags_entry = tk.Entry(task_details_window, textvariable=tk.StringVar(value=task_details[6]))
        tags_entry.grid(row=4, column=1)


root = tk.Tk()
root.title("Todo List App")

# Login/Register Frame
login_register_frame = tk.Frame(root)
login_register_frame.pack(fill=tk.BOTH, expand=True)

username_label = tk.Label(login_register_frame, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_register_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(login_register_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_register_frame, show="*")
password_entry.grid(row=1, column=1)

login_button = tk.Button(login_register_frame, text="Login", command=login)
login_button.grid(row=2, column=0)

register_button = tk.Button(login_register_frame, text="Register", command=register)
register_button.grid(row=2, column=1)

# Task Frame
task_frame = tk.Frame(root)

task_label = tk.Label(task_frame, text="Task:")
task_label.grid(row=0, column=0)
task_entry = tk.Entry(task_frame)
task_entry.grid(row=0, column=1)

due_date_day_var = tk.StringVar(root)
due_date_day_var.set("Day")
due_date_day_options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
due_date_day_dropdown = tk.OptionMenu(task_frame, due_date_day_var, *due_date_day_options)
due_date_day_dropdown.grid(row=1, column=0)

due_date_month_var = tk.StringVar(root)
due_date_month_var.set("Month")
due_date_month_options = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
due_date_month_dropdown = tk.OptionMenu(task_frame, due_date_month_var, *due_date_month_options)
due_date_month_dropdown.grid(row=1, column=1)

due_date_year_var = tk.StringVar(root)
due_date_year_var.set("Year")
due_date_year_options = ["2024", "2025", "2026", "2027", "2028", "2029", "2030"]
due_date_year_dropdown = tk.OptionMenu(task_frame, due_date_year_var, *due_date_year_options)
due_date_year_dropdown.grid(row=1, column=2)

priority_var = tk.StringVar(root)
priority_var.set("Priority")
priority_options = ["Low", "Medium", "High", "Urgent"]
priority_dropdown = tk.OptionMenu(task_frame, priority_var, *priority_options)
priority_dropdown.grid(row=2, column=0)

notes_label = tk.Label(task_frame, text="Notes:")  # Add notes label
notes_label.grid(row=3, column=0)
notes_entry = tk.Entry(task_frame)
notes_entry.grid(row=3, column=1)

tags_label = tk.Label(task_frame, text="Tags:")  # Add tags label
tags_label.grid(row=4, column=0)
tags_entry = tk.Entry(task_frame)
tags_entry.grid(row=4, column=1)

add_task_button = tk.Button(task_frame, text="Add Task", command=add_task_gui)
add_task_button.grid(row=5, column=0, columnspan=2)

task_listbox = tk.Listbox(task_frame)
task_listbox.grid(row=6, column=0, columnspan=2)

# Bind click event on task_listbox to show_task_details function
task_listbox.bind("<<ListboxSelect>>", show_task_details)

root.mainloop()