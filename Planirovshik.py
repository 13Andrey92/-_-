from tkinter import *


class General:
    def __init__(self, root):
        self.root = root
        self.root.geometry("350x290+1200+100")
        self.root.title("Планировщик")
        self.root.resizable(False, False)
        self.task_list = Listbox(self.root, width=50, height=14)
        self.task_list.pack(expand=True, anchor="center")
        self.new_task_button = Button(self.root, text="Новая задача", command=self.btn_click)
        self.new_task_button.pack(expand=True, anchor="center")

    def btn_click(self):
        self.task_panel = Tk()
        self.task_panel.geometry("200x130+1275+500")
        self.task_panel.title("Новая задача")
        self.task_panel.resizable(False, False)

        self.title = Label(self.task_panel, text="Название:")
        self.title.grid(column=0, row=0, sticky="w")
        self.description = Label(self.task_panel, text="Описание:")
        self.description.grid(column=0, row=1, sticky="w")
        self.priority = Label(self.task_panel, text="Приоритет:")
        self.priority.grid(column=0, row=2, sticky="w")
        self.status = Label(self.task_panel, text="Статус:")
        self.status.grid(column=0, row=3, sticky="w")

        self.title_entry = Entry(self.task_panel)
        self.title_entry.grid(column=1, row=0, sticky="e")
        self.description_entry = Entry(self.task_panel)
        self.description_entry.grid(column=1, row=1, sticky="e")
        self.priority_entry = Entry(self.task_panel)
        self.priority_entry.grid(column=1, row=2, sticky="e")
        self.status_entry = Entry(self.task_panel)
        self.status_entry.grid(column=1, row=3, sticky="e")

        send = Button(self.task_panel, text="Сохранить", command=self.save_file)
        send.grid(columnspan=2, row=5, sticky="s", padx=5, pady=10)

    def save_file(self):
        with open("task_scheduler.txt", "a", encoding="utf-8") as file:
            file.write("-" * 15 + "\n")
            file.write(f"Название: {self.title_entry.get()}\n")
            file.write(f"Описание: {self.description_entry.get()}\n")
            file.write(f"Приоритет: {self.priority_entry.get()}\n")
            file.write(f"Статус: {self.status_entry.get()}\n")

        self.task_list.insert(0, self.title_entry.get())
        self.task_panel.destroy()


root = Tk()
my_widget = General(root)
root.mainloop()
