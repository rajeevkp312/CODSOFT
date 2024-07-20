from tkinter import *
from tkinter import ttk

class Todo:
    def __init__(self, root):
        self.root = root
        self.root.title('To-do List')
        self.root.geometry('650x410+300+150')

        # Title label
        self.label = Label(self.root, text='To-Do-List-App', 
                           font='Arial, 25 bold', width=20, bd=5, bg='orange', fg="black")
        self.label.pack(side='top', fill=BOTH)

        # Add Task Label
        self.label2 = Label(self.root, text='Add Task', 
                            font='Arial, 18 bold', width=10, bd=5, bg='orange', fg="black")
        self.label2.place(x=40, y=54)

        # Tasks Label
        self.label3 = Label(self.root, text='Tasks', 
                            font='Arial, 18 bold', width=10, bd=5, bg="orange", fg="black")
        self.label3.place(x=320, y=54)

        # Listbox to display tasks
        self.main_text = Listbox(self.root, height=9, bd=5, width=23, 
                                 font="Arial, 20 italic bold")
        self.main_text.place(x=280, y=100)

        # Text widget for task entry
        self.text = Text(self.root, bd=5, height=2, width=30, font='Arial, 10 bold')
        self.text.place(x=20, y=120)

        # Add button
        self.button = Button(self.root, text="Add", font='Arial, 20 bold italic', 
                             width=10, bd=5, bg="orange", fg="black", command=self.add)
        self.button.place(x=30, y=180)

        # Delete button
        self.button2 = Button(self.root, text="Delete", font="Arial, 20 bold italic", 
                              width=10, bd=5, bg="orange", fg="black", command=self.delete)
        self.button2.place(x=30, y=280)

        # Load existing tasks from the file
        self.load_tasks()

    def add(self):
        content = self.text.get(1.0, END).strip()
        if content:
            self.main_text.insert(END, content)
            with open('data.txt', 'a') as file:
                file.write(content + '\n')
            self.text.delete(1.0, END)

    def delete(self):
        selected_task_index = self.main_text.curselection()
        if selected_task_index:
            task_to_delete = self.main_text.get(selected_task_index)
            self.main_text.delete(selected_task_index)
            with open('data.txt', 'r') as file:
                lines = file.readlines()
            with open('data.txt', 'w') as file:
                for line in lines:
                    if line.strip() != task_to_delete:
                        file.write(line)

    def load_tasks(self):
        try:
            with open("data.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    self.main_text.insert(END, line.strip())
        except FileNotFoundError:
            pass  # No file to read from, just continue

def main():
    root = Tk()
    ui = Todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
