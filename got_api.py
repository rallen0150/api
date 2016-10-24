import requests

# results = requests.get("http://anapioficeandfire.com/api/characters/")
# json_result = results.json()
# print(json_result)

def get_all_data(option, lookup="name"):
    url = "http://anapioficeandfire.com/api/{}/".format(option)
    while url:
        results = requests.get(url)
        json_result = results.json()

        for x in json_result:
            print(x[lookup])
        if input("-----------Enter to continue, or (n) for new option: "):
            break
        url = results.headers['link'].split(";")[0].replace('<', '').replace('>', '')

def get_specific_data(option, number):
    url = "http://anapioficeandfire.com/api/{}/{}".format(option, number)
    while url:
        results = requests.get(url)
        json_result = results.json()

        if option == "characters":
            print("""\nName: {} \nTitles: {} \nAllegiance: {} \nBorn: {} \nDied: {}""".format(json_result["name"], json_result["titles"],
                  json_result["allegiances"], json_result["born"], json_result["died"]))
        elif option == "books":
            print("""\nName: {} \nAuthors: {} \nNumber of Pages: {} \nDate Released: {} """.format(json_result["name"], json_result["authors"],
                  json_result["numberOfPages"], json_result["released"]))
        elif option == "houses":
            print("""\nHouse Name: {} \nRegion of Westros: {} \nHouse Coat of Arms: {} \nHouse Words: {} \nFounded: {} \nSeats: {}\nCurrent Lord: {}"""
                  .format(json_result["name"], json_result["region"], json_result["coatOfArms"], json_result["words"],
                  json_result["founded"], json_result["seats"], json_result["currentLord"]))
        else:
            print("Invalid Option!")
        if input("-----------(n) to choose new option: "):
            break

while True:
    specific = input("Would you like to see the whole (l)ist or (s)pecific object, or (exit)? ").lower()
    if specific == 'l':
        choice = input("What would you like to search for (characters), (books), or (houses)? ").lower()
        get_all_data(choice)
    elif specific == 's':
        choice = input("What would you like to search for (characters), (books), or (houses)? ").lower()
        num = input("Which id number? ")
        get_specific_data(choice, num)
    elif specific == 'exit':
        print("\nGOODBYE")
        break
    else:
        print("Invalid Option")
