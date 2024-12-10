import tkinter as tk
from tkinter import messagebox

# Functionality for To-Do List Manager
def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create main application window
app = tk.Tk()
app.title("To-Do List Manager")
app.geometry("400x400")

# Header Label
header_label = tk.Label(app, text="To-Do List Manager", font=("Arial", 16))
header_label.pack(pady=10)

# Task Entry Frame
entry_frame = tk.Frame(app)
entry_frame.pack(pady=10)

task_entry = tk.Entry(entry_frame, width=30, font=("Arial", 12))
task_entry.pack(side=tk.LEFT, padx=10)

add_button = tk.Button(entry_frame, text="Add Task", command=add_task, font=("Arial", 10))
add_button.pack(side=tk.LEFT)

# Task Listbox
task_listbox = tk.Listbox(app, width=50, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)

# Button Frame for Remove and Clear
button_frame = tk.Frame(app)
button_frame.pack(pady=10)

remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, font=("Arial", 10))
remove_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear All Tasks", command=clear_tasks, font=("Arial", 10))
clear_button.pack(side=tk.LEFT)

# Run the application
app.mainloop()
