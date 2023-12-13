import requests
url = "https://rickandmortyapi.com/api/character/2"
response = requests.get(url)
data = response.json()
print(data)
