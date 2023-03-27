import requests
import json

# Replace the <YOUR_API_TOKEN> with your actual API token
url = 'https://api.clashroyale.com/v1/players/%23<PLAYER_TAG>'
headers = {'Authorization': 'Bearer <YOUR_API_TOKEN>'}

response = requests.get(url, headers=headers)
data = json.loads(response.text)

trophies = data['trophies']
clan_name = data['clan']['name']

print(f'Player has {trophies} trophies and is in the clan {clan_name}.')
