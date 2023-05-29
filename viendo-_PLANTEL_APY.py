import requests

# Hacer una solicitud GET a la API de API-Football.com para obtener los datos del plantel
response = requests.get("https://api-football.com/v3/players", params={"team": "460", "league": "ARG1", "season": "2021"})

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido JSON de la respuesta
    data = response.json()

    # Verificar si se encontraron jugadores en el plantel
    if data["response"]:
        # Iterar sobre la lista de jugadores y mostrar los detalles en la terminal
        for player in data["response"]:
            player_name = player["player"]["name"]
            player_age = player["player"]["age"]
            player_nationality = player["player"]["nationality"]
            print(f"Nombre: {player_name} | Edad: {player_age} | Nacionalidad: {player_nationality}")
    else:
        print("No se encontraron jugadores en el plantel.")
else:
    print("Error al obtener los datos del plantel.")

