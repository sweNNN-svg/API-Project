from tkinter import *
from tkinter import ttk
import requests

def get_weather(city_label, temp_label, city):
    api_key = 'API_ANAHTARINIZ'
    params = {'q': city, 'appid': api_key, 'lang': 'tr', 'units': 'metric'}
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

    response = requests.get(url, params=params)

    data = response.json()

    city_label.config(text=f'Hava Durumu: {data["weather"][0]["description"]}')
    temp_label.config(text=f'Sıcaklık: {data["main"]["temp"]} Celsius')

def open_home_view(root):
    home_root = Toplevel(root)
    home_root.title('Home')
    home_root.geometry('500x500')

    city_label = Label(home_root, text='Hava Durumu: ')
    city_label.pack()

    temp_label = Label(home_root, text='Sıcaklık: ')
    temp_label.pack()

    # Şehir seçimini sağlamak için bir Combobox
    cities = ['ISTANBUL', 'ANKARA', 'IZMIR']  # İstediğiniz şehirleri ekleyin
    selected_city = StringVar()
    city_combobox = ttk.Combobox(home_root, textvariable=selected_city, values=cities)
    city_combobox.pack()

    # Butona tıklandığında seçilen şehir için hava durumu bilgilerini al
    def on_button_click():
        selected_city_value = selected_city.get()
        get_weather(city_label, temp_label, selected_city_value)

    button = Button(home_root, text='Hava Durumu Getir', command=on_button_click)
    button.pack()

    home_root.mainloop()
