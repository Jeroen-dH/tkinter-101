import tkinter
import time
gui = tkinter.Tk()
gui.title("Clock")
gui.geometry("800x300")

def tijd():
    current_time = time.strftime("%H:%M:%S")
    clock.configure(text= current_time)
    clock.after(200,tijd)
    
clock = tkinter.Label(
    gui,
    font=("aria",120),
    bg="Yellow",
    fg="black",
    
)
clock.pack(
    fill="both",
    padx=0,
    pady=0,
    expand=True
)

tijd()
gui.mainloop()