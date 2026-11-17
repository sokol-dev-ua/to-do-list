import tkinter as tk
import os

tasks = []
done_tasks = []

os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except FileNotFoundError:
    pass

try:
    file = open("done_tasks.txt", "r")
    for line in file:
        done_tasks.append(line.strip())
    file.close()
except FileNotFoundError:
    pass


def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks()
def remove_task():
    selected = listbox.curselection()
    if selected:
        number = selected[0]
        listbox.delete(number)
        tasks.pop(number)
        save_tasks()
def save_tasks():
    file = open("tasks.txt", "w")
    for task in tasks:
        file.write(task +"\n")
    file.close()
    file = open("done_tasks.txt", "w")
    for task in done_tasks:
        file.write(task + "\n")
    file.close()
def done_task():
    selected = listbox.curselection()
    if selected:
        number = selected[0]
        task = tasks.pop(number)
        listbox.delete(number)
        done_tasks.append(task)
        done_listbox.insert(tk.END, task)
        save_tasks()



window = tk.Tk()
window.title("To-Do List")
entry = tk.Entry(window, width=30)
entry.pack()
button = tk.Button(window, text="add task", command=add_task)
button.pack()
remove_button = tk.Button(window, text="remove task", command=remove_task)
remove_button.pack()

listbox = tk.Listbox(window, width=40)
listbox.pack()
for task in tasks:
    listbox.insert(tk.END, task)

done_button = tk.Button(window, text="done task", command=done_task)
done_button.pack()
done_label = tk.Label(window, text="Done tasks:")
done_label.pack()
done_listbox = tk.Listbox(window, width=40)
done_listbox.pack()
for task in done_tasks:
    done_listbox.insert(tk.END, task)

window.mainloop()
