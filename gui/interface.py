import tkinter as tk
from tkinter import ttk


class Interface(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("My App")
        self.geometry("600x600")
        self.resizable(width=False, height=False)

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Start Page", font=("TkDefaultFont", 16))
        label.pack(side="top", fill="x", pady=10)

        button1 = ttk.Button(self, text="Go to Page One",
                             command=lambda: controller.show_frame("PageOne"))
        button2 = ttk.Button(self, text="Go to Page Two",
                             command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()

class PageOne(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Page One", font=("TkDefaultFont", 16))
        label.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

class PageTwo(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = ttk.Label(self, text="Page Two", font=("TkDefaultFont", 16))
        label.pack(side="top", fill="x", pady=10)

        button = ttk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        button.pack()

if __name__ == "__main__":
    app = Interface()
    app.mainloop()