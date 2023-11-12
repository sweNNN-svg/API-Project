from tkinter import *
import views.home_view as home_view
import views.about_view as about_view

root = Tk()
root.title('API Project')
root.geometry('500x500')

def show_selected():
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
Button(root, text='Show Selected', command=show_selected).pack()

def open_home_window():
    home_view.open_home_view()

def open_about_window():
    about_view.open_about_view()

Button(root, text='Home', command=open_home_window).pack()
Button(root, text='About', command=open_about_window).pack()

root.mainloop()
