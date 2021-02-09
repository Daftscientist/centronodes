import requests

def duck():
    url = f'https://api.centronodes.com/quack/'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    response = (jsonResponse["url"])
    return response