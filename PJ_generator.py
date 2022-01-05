import requests
import pyfiglet as fig

print(fig.figlet_format("P. J generator"))

while True:
    print('press q or q to stop the madness')
    inp = input("I want to hear a joke about ... :").lower().strip()
    if inp == 'q':
        break
    # the search route for the api
    query_str = "&page=1&limit=1"
    url = "https://icanhazdadjoke.com/search?term="+inp+query_str
    resp = requests.get(url, 
            headers = {"Accept" : "application/json", 
            "User-Agent" : "practising api calls"}
            ).json()
    try:
        joke = resp["results"][0]['joke']
        print(joke)
    except IndexError:
        print(f"oh, I dont know any stupid jokes about {inp}. Ask me something else")
    #["joke"]
