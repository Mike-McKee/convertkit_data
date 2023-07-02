import api_secrets
import requests
import json

api_key = api_secrets.KEY
api_secret = api_secrets.SECRET

data = []
for i in range(1,3):
    response = requests.get(f'https://api.convertkit.com/v3/subscribers?api_secret={api_secret}&page={i}')
    reply = response.json()
    data.extend(reply['subscribers'])

with open('subscriber_data.json', 'w') as file:
    json.dump(data, file, indent=4)


print('-----------------SUCCESS-----------------')