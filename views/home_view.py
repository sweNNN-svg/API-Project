from tkinter import *

def open_home_view():
    homeWindow = Tk()
    homeWindow.title('Home')
    homeWindow.geometry('500x500')
    Label(homeWindow, text="This is a Home Window").pack()
    homeWindow.mainloop()
