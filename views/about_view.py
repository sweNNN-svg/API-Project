from tkinter import *


def open_about_view():
    aboutWindow = Tk()
    aboutWindow.title('About')
    aboutWindow.geometry('500x500')

    about_text = "Bu basit Python uygulaması, OpenWeather API kullanarak seçilen şehirin hava durumu bilgilerini görüntüler. Kullanıcı, Tkinter arayüzü üzerinden bir şehir seçer ve ardından bu şehrin güncel hava durumu bilgilerini API üzerinden alabilir."

    text_widget = Text(aboutWindow, wrap='word', width=50, height=10)
    text_widget.pack(padx=10, pady=10)

    text_widget.insert('1.0', about_text)

    aboutWindow.mainloop()