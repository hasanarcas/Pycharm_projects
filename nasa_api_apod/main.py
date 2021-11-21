import requests
from urllib.request import urlretrieve
from pprint import PrettyPrinter
import webbrowser

pp = PrettyPrinter()

api_key = "QNiqK7NtFFA9SCe4O84PiAVTPg5SKTLxbs538Dzn"

def fetchAPOD():
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date= "2021-11-21"
    params = {
        'api_key': api_key,
        'date': date,
        'hd': 'True'
    }
    response = requests.get(URL_APOD, params=params).json()
    return response

#responseAPOD = fetchAPOD()
#open_url_apod = responseAPOD["hdurl"]
#webbrowser.open(open_url_apod)


def fetchAsteroidsNeows():
    URL_NEO_FEED = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        'api_key': api_key,
        'start_date':'2020-01-22',
        'end_date':'2020-01-23'
    }

    response = requests.get(URL_NEO_FEED, params=params).json()
    pp.pprint(response)

#fetchAsteroidsNeows()


def fetchEPICData():
  URL_EPIC = "https://api.nasa.gov/EPIC/api/natural/"
  params = {
      'api_key':api_key,
  }
  response = requests.get(URL_EPIC, params=params).json()
  pp.pprint(response)

#fetchEPICData()

def fetchEPICImage():
  YEAR = '2015'
  MONTH = '10'
  DAY = '31'
  IMAGE_ID = 'epic_1b_20151031074844'
  URL_EPIC = "https://epic.gsfc.nasa.gov/archive/natural/"
  URL_EPIC = URL_EPIC + YEAR +'/' + MONTH + '/'+DAY
  URL_EPIC = URL_EPIC + '/png'
  URL_EPIC = URL_EPIC + '/' + IMAGE_ID + '.png'
  print(URL_EPIC)
  urlretrieve(URL_EPIC,IMAGE_ID+'.png')

fetchEPICImage()