import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import Calendar, DateEntry
import datetime

# Initialize the main window
root = tk.Tk()
root.title("Task Master Application")
root.configure(bg="lightblue")

# List to store tasks
tasks = []

# Function to add a task
def add_task():
    task = entry.get()
    priority = priority_var.get()
    deadline = calendar.get_date()
    today = datetime.date.today()

    if task != "" and priority != "Select Priority" and deadline >= today:
        tasks.append({"task": task, "priority": priority, "deadline": deadline.strftime('%Y-%m-%d')})
        update_task_listbox()
        entry.delete(0, tk.END)
        entry.insert(0, "Enter a task")
    else:
        messagebox.showwarning("Warning", "Please enter a task, priority, and a valid deadline.")

# Function to edit a selected task
def edit_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        selected_task = tasks[selected_task_index[0]]
        new_task = simpledialog.askstring("Edit Task", "Edit the task:", initialvalue=selected_task["task"])
        new_priority = simpledialog.askstring("Edit Priority", "Edit the priority (High, Medium, Low):", initialvalue=selected_task["priority"])
        new_deadline = simpledialog.askstring("Edit Deadline", "Edit the deadline (YYYY-MM-DD):", initialvalue=selected_task["deadline"])
        if new_task and new_priority and new_deadline:
            tasks[selected_task_index[0]] = {"task": new_task, "priority": new_priority, "deadline": new_deadline}
            update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

# Function to delete a selected task
def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        del tasks[selected_task_index[0]]
        update_task_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Function to update the listbox display
def update_task_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        display_text = f"{task['task']} - Priority: {task['priority']} - Deadline: {task['deadline']}"
        listbox.insert(tk.END, display_text)

# Function to show the help documentation
def show_help():
    help_text = (
        "Task Master Application Help\n\n"
        "1. Add Task: Enter a task in the input box, select a priority, set a deadline, and click 'Add Task'.\n"
        "2. Edit Task: Select a task from the list, then click 'Edit Task' and enter the new task details.\n"
        "3. Delete Task: Select a task from the list and click 'Delete Task'.\n"
    )
    messagebox.showinfo("Help", help_text)

# Function to exit the application
def exit_app():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

# Main frame
main_frame = tk.Frame(root, bg="lightblue")
main_frame.pack(padx=10, pady=10)

# Left frame for options
left_frame = tk.Frame(main_frame, bg="lightblue")
left_frame.pack(side=tk.LEFT, padx=10)

# Entry widget for task input with watermark
entry = tk.Entry(left_frame, width=30, fg='grey')
entry.insert(0, "Enter a task")
entry.bind("<FocusIn>", lambda event: entry.delete(0, tk.END) if entry.get() == "Enter a task" else None)
entry.bind("<FocusOut>", lambda event: entry.insert(0, "Enter a task") if entry.get() == "" else None)
entry.pack(pady=5)

# Dropdown for priority selection
priority_var = tk.StringVar()
priority_var.set("Select Priority")
priority_menu = tk.OptionMenu(left_frame, priority_var, "High", "Medium", "Low")
priority_menu.pack(pady=5)

# Calendar widget for deadline input
calendar = DateEntry(left_frame, width=30, mindate=datetime.date.today(), date_pattern='yyyy-mm-dd')
calendar.pack(pady=5)

# Buttons for actions
add_button = tk.Button(left_frame, text="Add Task", command=add_task, bg="lightgreen")
add_button.pack(pady=5)

edit_button = tk.Button(left_frame, text="Edit Task", command=edit_task, bg="lightpink")
edit_button.pack(pady=5)

delete_button = tk.Button(left_frame, text="Delete Task", command=delete_task, bg="lightcoral")
delete_button.pack(pady=5)

# Right frame for task list
right_frame = tk.Frame(main_frame, bg="lightblue")
right_frame.pack(side=tk.RIGHT, padx=10)

# Listbox to display tasks
listbox = tk.Listbox(right_frame, width=50, height=15, bd=0, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(right_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create a menu bar
menubar = tk.Menu(root)
root.config(menu=menubar)

# Add 'Help' and 'Exit' to the menu bar
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="How to Use", command=show_help)
help_menu.add_separator()
help_menu.add_command(label="Exit", command=exit_app)

# Run the main event loop
root.mainloop()
