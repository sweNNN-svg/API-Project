from tkinter import *

def open_about_view():
    aboutWindow = Tk()
    aboutWindow.title('About')
    aboutWindow.geometry('500x500')
    Label(aboutWindow, text="This is an About Window").pack()
    aboutWindow.mainloop()
