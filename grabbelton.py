import tkinter
import random

gui = tkinter.Tk()
gui.title("grabbelton")
gui.configure(bg="#8296C8")
gui.geometry("500x250")
itemslist = ["1 euro","2 euro","3 euro","4 euro","5 euro","6 euro","7 euro","8 euro","9 euro","10 euro"]
amount = len(itemslist)

def onclick():
    global keuze
    keuze = random.choice(itemslist)
    itemslist.remove(keuze)
    print(keuze)
    amount = len(itemslist)
    aantalitems.config(text="Er zitten nog "+ str(amount) +" items in de grabbelton")
    itemgrabbel.config(text="Je hebt "+str(keuze)+" gegrabbeld",bg="#6496C8",relief="solid")
    itemgrabbel.pack()
    if amount == 0:
        button.destroy()
        aantalitems.config(text="Er zitten geen items meer in de grabbelton")
    
            
# label die laat zien hoeveel items er in zitten
aantalitems = tkinter.Label(
    gui,
    text="Er zitten nog "+ str(amount) +" items in de grabbelton",
    bg="#8296C8",
    fg= "Black",
    font=("arial",20)
)
aantalitems.pack(side="top")

#De "grabbel" knop
button = tkinter.Button(gui)
button.configure(text="Grabbelen", command=onclick)
button.pack(padx=125,pady=50,)

y = tkinter.Label(
    gui,
    text="Het item dat je hebt getrokken is:",
    font=("arial", 10),
    bg="#6497C8",
    fg="Black",
    borderwidth="2",
    relief="solid"
)
y.pack(padx=30,pady=10)

itemgrabbel = tkinter.Label(gui,text="")   
 
gui.mainloop()
