import tkinter as tk
from tkinter import messagebox, simpledialog

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(
            self.frame, 
            width=50, 
            height=15, 
            bd=0, 
            font=('Helvetica', 14), 
            selectbackground='#a6a6a6'
        )
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry = tk.Entry(
            self.root, 
            font=('Helvetica', 14), 
            width=34, 
            bd=0
        )
        self.entry.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.add_task_button = tk.Button(
            self.button_frame, 
            text='Add Task', 
            font=('Helvetica', 14), 
            bg='#c5f776', 
            padx=20, 
            pady=10, 
            command=self.add_task
        )
        self.add_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.delete_task_button = tk.Button(
            self.button_frame, 
            text='Delete Task', 
            font=('Helvetica', 14), 
            bg='#ff8b61', 
            padx=20, 
            pady=10, 
            command=self.delete_task
        )
        self.delete_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

        self.clear_task_button = tk.Button(
            self.button_frame, 
            text='Clear Tasks', 
            font=('Helvetica', 14), 
            bg='#ff6b61', 
            padx=20, 
            pady=10, 
            command=self.clear_tasks
        )
        self.clear_task_button.pack(fill=tk.BOTH, expand=True, side=tk.LEFT)

    def add_task(self):
        task = self.entry.get()
        if task != "":
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.task_listbox.delete(selected_task_index)
        except:
            messagebox.showwarning("Warning", "You must select a task.")

    def clear_tasks(self):
        self.tasks = []
        self.task_listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
