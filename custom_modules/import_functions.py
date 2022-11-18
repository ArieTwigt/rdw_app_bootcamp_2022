import requests

# method for getting the cars
def get_car(kenteken):

    kenteken_upper = kenteken.upper()

    endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={kenteken_upper}"

    response = requests.get(endpoint)

    data = response.json()

    return data[0]