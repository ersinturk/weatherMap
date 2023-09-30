import requests
from tkinter import *

window = Tk()
window.geometry("400x500")
window.resizable(0,0)
window.title("Weather App")

city_value = StringVar()

def weatherInfo():
    api_key = "9929e87937be016f477297a53c74d9f1"
    city = city_value.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    info_text.delete("1.0", "end")

    if response.status_code == 200:
        kelvin = 273
        temp = int(data["main"]["temp"] - kelvin)
        feels_temp = int(data["main"]["feels_like"] - kelvin)
        desc = data["weather"][0]["description"]

        weather_read = f"\nWeather of: {city}\nTemprature (c): {temp}°\nFeels Like in (c): {feels_temp}°\nInfo: {desc}"
    else:
        weather_read = f"\n\tWeather for '{city}' not found!\n\tPlease Enter Valid City!"

    info_text.insert(INSERT, weather_read)


##### #FRONTEND PART OF CODE #####
icon = PhotoImage(file="weather_icon.png")
icon_label = Label(window, image=icon)
icon_label.pack()


city_label = Label(window, text="Enter City Name", font="Helvetica 12 bold")
city_label.pack(pady=10)

city_entry = Entry(window, textvariable=city_value, width=43,  font="Helvetica 14 normal")
city_entry.pack()

weather_button = Button(window, text = "Check Weather", command=weatherInfo, font="Helvetica 12", padx=5, pady=5)
weather_button.pack(pady= 20)

weather_label = Label(window, text= "The Weather is:", font="Helvetica 12 bold")
weather_label.pack(pady=10)

info_text = Text(window, font="Helvetica 20 normal", width=50, height=10)
info_text.pack(pady=10, padx=10)


window.mainloop()