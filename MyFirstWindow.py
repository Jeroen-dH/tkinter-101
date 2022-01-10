import tkinter 
import time
gui = tkinter.Tk() 
a = 0
b = 50
c = 50
colors = ["white","yellow","orange","red","purple","black",""]
#sets title for window

gui.title("My first window")
gui.geometry("50x50")
gui.configure(bg="white")

def veranderaar():
    global a, b, c
    gui.configure(bg=colors[a])
    gui.geometry(str(b) + "x" + str(c))
    b += 50
    c += 50
    a += 1
    print(7-a)
    if a >= 7:
        time.sleep(1)
        print("Boom")
        gui.destroy()
        
        
       


for x in range(7):
    gui.after(1000*x, veranderaar)

    

gui.mainloop()    
    


