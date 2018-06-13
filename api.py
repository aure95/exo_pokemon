#/usr/bin/python3

import hug

from bs4 import BeautifulSoup

with open("pokemon.html") as file:
    soup = BeautifulSoup(file,"lxml")
    soup.find(id="pokedex")

    for tab in  soup.find_all("tr"):
        for data in tab.find_all("td"):
            print(data.text)
            print("\n")

















print("coucou ")