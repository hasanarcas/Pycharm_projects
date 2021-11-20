import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import webbrowser

pp = PrettyPrinter()

api_key = "QNiqK7NtFFA9SCe4O84PiAVTPg5SKTLxbs538Dzn"

def fetchAPOD():
    url_apod = "https://api.nasa.gov/planetary/apod"
    date= "2021-11-19"
    params = {
        'api_key': api_key,
        'date': date,
        'hd': 'True'
    }
    response = requests.get(url_apod, params=params).json()
    return response
responseAPOD = fetchAPOD()

open_url_apod = responseAPOD["hdurl"]
webbrowser.open(open_url_apod)

