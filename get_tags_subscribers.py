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
        response = requests.get(f'https://api.convertkit.com/v3/tags/{i["id"]}/subscriptions?api_secret={api_secret}')
        r = response.json()
        if r['total_pages'] > 1:
            ran = int(r['total_pages'])
            for j in range (1, ran + 1):
                new_response = requests.get(f'https://api.convertkit.com/v3/tags/{i["id"]}/subscriptions?api_secret={api_secret}&page={j}')
                new_r = new_response.json()
                temp = {i['name']:new_r}
                tag_info.append(temp)
        else:
            temp = {i['name']:r}
            tag_info.append(temp)

with open('SUBSCRIBER_DATA/tags_data.json', 'w') as new_file:
    json.dump(tag_info, new_file, indent=4)


print('-----------------SUCCESS-----------------')