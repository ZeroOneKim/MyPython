from tkinter import *
from tkinter import messagebox

def function():
    messagebox.showinfo("Button title", "Hello.~~~")

window = Tk()

buttonVar = Button(window, text = "click it", command = function)
buttonVar.pack()

#********if you want make checkbutton ~************
#def function2():
#    if chk.get() == 0:
#        messagebox.showinfo("", "turn off the check btn")
#    else:
#        messagebox.showinfo("", "turn on ~~")

#chk = IntVar()
#var = Checckbutton(window, text = "클릭(Click)", variable = chk, command = function2)
#var.pack()

window.mainloop()
