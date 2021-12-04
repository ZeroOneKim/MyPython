from tkinter import *   #tkinter => close at window programming

window = Tk()
window.title(" Title Name ") #title
window.geometry("400x100") #window size
window.resizable(width= FALSE, height= FALSE) #Can't rechange the win's size

var = Label(window, text  = "Text Message ~ ~") #add a message
var.pack()
var2 = Label(window, text = "Tool", font = ("굴림체", 25), bg = "red", fg="blue", anchor=SE)
var2.pack()     #if you want transform that message > add it. width =???  height = ???

#********* add photo tool************
#photoVar = PhotoImage(file = "C:/ 경로")   #PC -> photoVar -> var -> expression
#var = Label(window, image = photoVar)
#var.pack()

#********* add Button tool ************
#buttonVar = Button(window, text = "내용", command = 명령~)
#buttonVar.pack()

window.mainloop()
