import api_secrets
import requests
import json
import time

start = time.time()

api_key = api_secrets.KEY
api_secret = api_secrets.SECRET

def list_broadcasts():

    response = requests.get(f'https://api.convertkit.com/v3/broadcasts?page=1&api_secret={api_secret}')
    data = response.json()
    d = data['broadcasts']

    response_2 = requests.get(f'https://api.convertkit.com/v3/broadcasts?page=2&api_secret={api_secret}')
    data_2 = response_2.json()
    d_2 = data_2['broadcasts']

    list_of_broadcasts = []

    for i in d:
        list_of_broadcasts.append(i)
    for j in d_2:
        list_of_broadcasts.append(j)
    
    broadcasts = {'broadcasts':list_of_broadcasts}
    
    return broadcasts

def broadcast_stats():
    
    data = list_broadcasts()
    d = data['broadcasts']
    stats= []

    for i in d:
        response = requests.get(f'https://api.convertkit.com/v3/broadcasts/{i["id"]}/stats?api_secret={api_secret}')
        r = response.json()
        stats.append(r['broadcast'])

    return stats


def specific_broadcast():
    
    data = list_broadcasts()
    d = data['broadcasts']
    specific_broadcasts = []

    for i in d:
        response = requests.get(f'https://api.convertkit.com/v3/broadcasts/{i["id"]}?api_secret={api_secret}')
        r = response.json()
        specific_broadcasts.append(r['broadcast'])
    
    return specific_broadcasts

def main():

    with open('SUBSCRIBER_DATA/list_of_broadcasts.json', 'w') as file_1:
        data_1 = list_broadcasts()
        json.dump(data_1, file_1, indent=4)

    with open('SUBSCRIBER_DATA/broadcast_stats.json', 'w') as file_2:
        data_2 = broadcast_stats()
        json.dump(data_2, file_2, indent=4)
    
    with open('SUBSCRIBER_DATA/specific_broadcasts.json', 'w') as file_3:
        data_3 = specific_broadcast()
        json.dump(data_3, file_3, indent=4)

    
main()

end = time.time()
total_time = round(end - start)
print("---------------------- success ----------------------")
print(f'Total program runtime = {total_time} seconds.')
