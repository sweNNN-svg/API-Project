from tkinter import *

import views

root = Tk()
root.title('API Project')
root.geometry('500x500')

def showSelected():
    itm = lb.get(lb.curselection())
    var.set(itm)

var = StringVar()
lb = Listbox(root)
lb.pack()

lb.insert(0, 'Iceland')
lb.insert(1, 'USA')
lb.insert(2, 'China')
lb.insert(3, 'Europe')


disp = Label(root, textvariable=var)
disp.pack(pady=20)
Button(root, text='Show Selected', command=showSelected).pack()

def openHomeWindow():
    homeWindow = Toplevel(root)
    homeWindow.title("Home Window")
    homeWindow.geometry("500x500")
    Label(homeWindow,
          text="This is a Home Window").pack()


Button(root, text='Home', command=views.home_view).pack()
Button(root, text='About', command=views.about_view).pack()


root.mainloop()