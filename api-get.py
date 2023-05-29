import requests

url = "https://api-football-v1.p.rapidapi.com/v2/leagues/country/albania"

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "YOUR RAPID API KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)