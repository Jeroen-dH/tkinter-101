import tkinter
from tkinter import ttk
gui = tkinter.Tk()
gui.title("Hello!")
gui.config(bg="Blue")
gui.geometry("250x200")

textbox = tkinter.Label(
    gui,
    text="Hello tkinter!",
    bg="red",
    fg="black",
    width=49

    
)
textbox.pack(
    fill= "both",
    padx=30,
    pady=40,
    expand=True
)

gui.mainloop()