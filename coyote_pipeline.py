# Lotek API access

import requests

payload = {'username': 'MPGCoyotes', 
            'password': 'Gogriz20$4'}

r = requests.post('https://webservice.lotek.com/API/user/login', params=payload)

print(r)

requests.post('https://webservice.lotek.com/API/user/login', params=payload)
