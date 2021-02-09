  
from requests.exceptions import HTTPError
import requests


def ram(user_id):
    url = f'https://api.centronodes.com/1.0/index.php?user_id={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    response = (jsonResponse["ram"])
    return response

def disk(user_id):
    url = f'https://api.centronodes.com/1.0/index.php?user_id={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    response = (jsonResponse["disk"])
    return response

def cores(user_id):
    url = f'https://api.centronodes.com/1.0/index.php?user_id={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    response = (jsonResponse["cores"])
    return response

def servers(user_id):
    url = f'https://api.centronodes.com/1.0/index.php?user_id={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    response = (jsonResponse["servers"])
    return response

def coins(user_id):
    url = f'https://api.centronodes.com/1.0/index.php?user_id={user_id}'
    response = requests.get(url)
    response.raise_for_status()
    jsonResponse = response.json()
#<----------------------------------->
    response = (jsonResponse["coins"])
    return response

