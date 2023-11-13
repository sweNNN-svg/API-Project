from tkinter import *
import views.home_view as home_view
import views.about_view as about_view

root = Tk()
root.title('API Project')
root.geometry('500x500')

def open_home_window():
    home_view.open_home_view(root)

def open_about_window():
    about_view.open_about_view()

home_but = Button(root, text='Home', command=open_home_window)
about_but = Button(root, text='About', command=open_about_window)

home_but.place(relx=0.5, rely=0.4, anchor=CENTER)
about_but.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()
