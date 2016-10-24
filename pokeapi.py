import requests

# results = requests.get("http://pokeapi.co/api/v2/pokemon/")
# json_result = results.json()
# print(json_result)

def get_all_pokemon_data(option, start="name"):
    url = "http://pokeapi.co/api/v2/{}/".format(option)
    # print(json_result["results"])
    while url:
        results = requests.get(url)
        json_result = results.json()

        for pokemon in json_result["results"]:
            print(pokemon[start])

        url = json_result["next"]

def get_specific_pokemon_data(option, number, start="name"):
    url = "http://pokeapi.co/api/v2/{}/{}/".format(option, number)
    # print(json_result["results"])
    while url:
        results = requests.get(url)
        json_result = results.json()
        number = id
        for pokemon in json_result["results"]:
            print(pokemon[start])

        url = json_result["next"]

while True:
    choice = input("What would you like to search for? ").lower()
    # get_all_pokemon_data(choice)
    specific = input("Would you like to view the (l)ist or a (s)pecific one? ").lower()
    if specific == 'l':
        get_all_pokemon_data(choice)
    else:
        num = input("What number do you want to see? ")
        get_specific_pokemon_data(choice, num)
        # pass
