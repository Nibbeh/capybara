import requests
import json

api_url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(api_url)

if response.status_code == 200:
    
    joke_data = json.loads(response.text)
    joke = joke_data['value']  
    print("Chuck Norris Joke:")
    print(joke)
else:
    print(f"Failed to get joke. Error: {response.status_code}")