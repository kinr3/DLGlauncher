import tkinter as tk
from tkinter import ttk as ttk


class Handler(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        HEIGHT = 720
        WIDTH = 1280
        background_image = tk.PhotoImage(file='image/Launcher1.png')
        container = ttk.Frame(self, height=HEIGHT, width=WIDTH)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in frames_list:

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FrameOne)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class FrameOne(tk.Frame):

    def __init__(self, parent, cotroller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="hi", font=LARGE_FONT)
        label.pack(pady=30, padx=30)

        button_switsch = ttk.Button(self, text='Button', command=lambda: cotroller.show_frame(FrameOne))
        button_switsch.pack()


if __name__ == "__main__":
    LARGE_FONT = ("Arial", 12)
    frames_list = (FrameOne, )
    app = Handler()
    app.mainloop()

