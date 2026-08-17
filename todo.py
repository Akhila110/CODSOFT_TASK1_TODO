import tkinter as tk
from tkinter import messagebox

tasks = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def update_list():
    task_list.delete(0, tk.END)
    for task in tasks:
        task_list.insert(tk.END, task)

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        update_list()
    except FileNotFoundError:
        pass

def add_task():
    task = task_entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    tasks.append(task)
    update_list()
    save_tasks()
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = task_list.curselection()[0]
        tasks.pop(index)
        update_list()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Please select a task!")

def update_task():
    try:
        index = task_list.curselection()[0]
        new_task = task_entry.get().strip()

        if new_task == "":
            messagebox.showwarning("Warning", "Please enter updated task!")
            return

        tasks[index] = new_task
        update_list()
        save_tasks()
        task_entry.delete(0, tk.END)

    except:
        messagebox.showwarning("Warning", "Please select a task!")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Clear all tasks?"):
        tasks.clear()
        update_list()
        save_tasks()

def select_task(event):
    try:
        index = task_list.curselection()[0]
        task_entry.delete(0, tk.END)
        task_entry.insert(0, tasks[index])
    except:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x550")
root.configure(bg="#EAF6F6")

title = tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 22, "bold"),
    bg="#EAF6F6",
    fg="darkblue"
)
title.pack(pady=10)

task_entry = tk.Entry(root, width=35, font=("Arial", 14))
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#EAF6F6")
button_frame.pack()

tk.Button(button_frame, text="Add", width=10, bg="lightgreen",
          command=add_task).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Update", width=10, bg="lightblue",
          command=update_task).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Delete", width=10, bg="tomato",
          command=delete_task).grid(row=0, column=2, padx=5)

tk.Button(root, text="Clear All", width=20, bg="orange",
          command=clear_tasks).pack(pady=10)

frame = tk.Frame(root)
frame.pack()

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_list = tk.Listbox(
    frame,
    width=40,
    height=12,
    font=("Arial", 14),
    yscrollcommand=scrollbar.set
)

task_list.pack(side=tk.LEFT)
scrollbar.config(command=task_list.yview)

task_list.bind("<<ListboxSelect>>", select_task)

load_tasks()

root.mainloop()