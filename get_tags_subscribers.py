import api_secrets
import requests
import json

api_key = api_secrets.KEY
api_secret = api_secrets.SECRET

with open('SUBSCRIBER_DATA/list_of_tags.json', 'r') as file:
    data = json.load(file)
    tags = data['tags']
    tag_info = []

    for i in tags:
        response = requests.get(f'https://api.convertkit.com/v3/tags/{i["id"]}/subscriptions?api_secret=<{api_secret}>')
        r = response.json()
        temp = {i['name']:r}
        tag_info.append(temp)

print(tag_info)

print('-----------------SUCCESS-----------------')