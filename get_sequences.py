import api_secrets
import requests
import json

api_key = api_secrets.KEY
api_secret = api_secrets.SECRET

response = requests.get(f'https://api.convertkit.com/v3/sequences?api_key={api_key}')
data = response.json()

with open('SUBSCRIBER_DATA/list_of_sequences.json', 'w') as file:
    json.dump(data, file, indent=4)

print('-----------------SUCCESS-----------------')