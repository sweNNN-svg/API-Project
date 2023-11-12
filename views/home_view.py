# views/home_view.py

from tkinter import *
import requests

def open_home_view():
    root = Tk()
    root.title('Home')
    root.geometry('500x500')

    # API çağrısı
    api_key = 'API_ANAHTARINIZ'
    city = 'ISTANBUL'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url)
    data = response.json()

    # API'den gelen verileri işleyerek ekrana bastırma
    Label(root, text=f'Hava Durumu: {data["weather"][0]["description"]}').pack()
    Label(root, text=f'Sıcaklık: {data["main"]["temp"]} Kelvin').pack()

    root.mainloop()
