import api_secrets
import requests
import json

api_key = api_secrets.KEY
api_secret = api_secrets.SECRET

tags_list_response = requests.get(f'https://api.convertkit.com/v3/tags?api_key={api_key}')
data = tags_list_response.json()

with open('list_of_tags.json', 'w') as file:
    json.dump(data, file, indent=4)

print('-----------------SUCCESS-----------------')