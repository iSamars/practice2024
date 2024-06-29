import tkinter as tk
from tkinter import ttk
from controller import Controller


class Application(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master = master
        self.master.geometry("400x500")
        self.master.title("Image processing")
        self.master.resizable(False, False)
        self.master.columnconfigure(index=0, weight=0)
        self.controller = Controller(self)
        for c in range(2):
            self.master.columnconfigure(index=c, weight=1)
        self.master.rowconfigure(index=0, weight=5)
        self.master.rowconfigure(index=1, weight=5)
        self.master.rowconfigure(index=2, weight=5)
        self.master.rowconfigure(index=3, weight=85)
        self.imagebox = None

        self.create_widgets()

    # Draw UI elements
    def create_widgets(self):
        ttk.Button(
            text="Открыть изображение",
            command=self.controller.open_image,
            width=350
        ).grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        ttk.Button(
            text="Сделать фото",
            command=self.controller.capture_image,
            width=350
        ).grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        ttk.Button(
            text="Негатив",
            width=20,
            command=self.controller.negative_image
        ).grid(row=2, column=0)

        ttk.Button(
            text="Повысить яркость",
            width=20,
            command=self.controller.increase_brightness,
        ).grid(row=2, column=1)

        ttk.Button(
            text="Нарисовать круг", width=20, command=self.controller.draw_circle
        ).grid(row=2, column=2)

        self.imagebox = tk.Label(self.master, bg="lightgray")
        self.imagebox.grid(
            row=3, column=0, columnspan=3, padx=5, pady=5, sticky="NSEW"
        )

    def callBack(self):
        pass


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
