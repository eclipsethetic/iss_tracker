import requests
import turtle
import time

link = 'http://api.open-notify.org/iss-now.json'

def get_data(link='http://api.open-notify.org/iss-now.json'):
    while True:
        try:
            response = requests.get(link)
            break
        except:
            time.sleep(1)
            continue
    _data = response.json()

    latitude = _data["iss_position"]["latitude"]
    longitude = _data["iss_position"]["longitude"]

    data = [latitude, longitude]

    return data


def iss_on_map():
    screen = turtle.Screen()
    screen.setup(1280, 720)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.bgpic("pics/map.gif")
    screen.title("ISS Tracker")
    screen.register_shape('pics/new_iss.gif',)
    iss = turtle.Turtle()
    iss.penup()
    iss.shape('pics/new_iss.gif')
        
    while True:
        x = float(get_data()[1])
        y = float(get_data()[0])
        time.sleep(3)
        iss.goto(x, y)
    
    