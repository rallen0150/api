import requests

def get_pokemon_data(option):
    url = "http://pokeapi.co/api/v2/{}/".format(option)

    # print(json_result["results"])
    while url:
        results = requests.get(url)
        json_result = results.json()

        for pokemon in json_result["results"]:
            print(pokemon["name"])


        url = json_result["next"]

while True:
    choice = input("What would you like to search for? ")
    get_pokemon_data(choice)
