import socket
import json
from decimal import Decimal
import sys

def connect():
    host = "api.openweathermap.org"
    port = 80

    city = sys.argv[2]
    key = sys.argv[1]
    request = "GET /data/2.5/weather?q=" + city + "&APPID=" + key + "&units=metric HTTP/1.0\r\n\r\n"
    request = bytes(request, 'utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request)
        out = s.recv(1024)
        return out


def output(out):
    out = str(out)
    out = out.split("\\r\\n")
    idata = out[-1]
    idata = idata[:-1]
    fdata = json.loads(idata)
    if fdata["cod"] != 200:
        return fdata["cod"]
    weather = (fdata["weather"][0])
    print(sys.argv[2])
    try:
        print("overcast: " + weather["description"])
    except:
        print("overcast: data unavailable")
    try:
        print("temp: " + str(fdata["main"]["temp"]) + "°C")
    except:
        print("temp: data unavailable")
    try:    
        print("humidity: " + str(fdata["main"]["humidity"]) + "%")
    except:
        print("humidity: data unavailable")
    try:
        print("pressure: " + str(fdata["main"]["pressure"]) + "hPa")
    except:
        print("pressure: data unavailable")
    try:    
        w_speed = Decimal(fdata["wind"]["speed"] * 3.6)
        w_speed = round(w_speed, 2)
        print("wind-speed: " + str(w_speed) + "km/h")
    except:
        print("wind-speed: data unavailable")
    try:
        print("wind-deg: " + str(fdata["wind"]["deg"]))
    except:
        print("wind-deg: data unavailable")


data = connect()
output(data)
