import tkinter

clickcounter = 0
gui = tkinter.Tk()
gui. geometry("400x500")
gui.title("Clicker V1")
gui.configure(
    bg="gray"
)

def colorchanger():
    if clickcounter < 0:
        gui.configure(bg="red")
    elif clickcounter > 0:
        gui.configure(bg="#00DC00")
    else:
        gui.configure(bg="gray")

# de up button

def up():
    global clickcounter
    clickcounter += 1
    counter.config(text=clickcounter)
    counter.pack()
    gui.after(10, colorchanger)
    

button1 = tkinter.Button(gui, font=("arial", 20, "bold"), command= up)
button1.configure(
    text="Up",
    bg=("#00DC00"),
    padx= 30
)
button1.pack(
    pady= 30
)

# de counter in het midden     

counter = tkinter.Label(
    gui,
    text=clickcounter,
    padx=80,
    pady=30,
    font=("arial", 30, "bold"),
    borderwidth=2,
    relief="solid"
)
counter.pack(
    
)

# de Down button
def down():
    global clickcounter
    clickcounter =clickcounter - 1
    counter.config(text=clickcounter)
    counter.pack()
    gui.after(10, colorchanger)
    

button2 = tkinter.Button(
    gui,
    text="down",
    font=("arial", 30, "bold"),
    command= down,
    bg="red"
)
button2.pack(
    pady=30
)

gui.mainloop()