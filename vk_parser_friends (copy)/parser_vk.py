import requests
import json
from database import create_database_friends

TOKEN_USER = "Скрыл токен"
VERSION = "5.131"


url_friends = f"https://api.vk.com/method/friends.get?extended=1&v=5.124&access_token={TOKEN_USER}&fields=photo_50"
url_subs = f"https://api.vk.com/method/friends.getRequests?extended=1&v=5.124&access_token={TOKEN_USER}&need_viewed=1"

friends_lst = []
subs_lst = []

def get_friends():
    response = requests.get(url_friends,
    params = {
        "v": VERSION
    })
    data = response.json()['response']['items']
    for el in data:
        first_name = el["first_name"]
        last_name = el["last_name"]
        photo = el["photo_50"]
        friends_lst.append((first_name, last_name, photo))

def get_subs(): 
    response = requests.get(url_subs,
    params = {
        "v": VERSION
    })
    data = response.json()['response']['items']
    for el in data:
        first_name = el["first_name"]
        last_name = el["last_name"]
        sub_id = el["user_id"]
        subs_lst.append((first_name, last_name, sub_id))

get_friends()
get_subs()
create_database_friends(friends=friends_lst, subs=subs_lst)