#/usr/bin/python3

import hug

from bs4 import BeautifulSoup

#////////////////////////////////////////////////////////////////////
class Pokemon:
        name=""
        type=""
        total=""
        attack=""
        defense=""
        sp_attack=""
        sp_defense=""
        speed=""
        speed=""
'''
#pass= permet de redefinir constructeur
def __init__(self):

    pass
'''
def __init__(self,name,type,total,attack,defense,sp_attack,sp_defense,speed ):

    self.name=name
    self.type=type
    self.total=total
    self.attack=attack
    self.defense=defense
    self.sp_attack=sp_attack
    self.sp_defense=sp_defense
    self.speed=speed
    pass

#/////////////////////////////////////////////////////////////
    with open("pokemon.html") as file:
        soup = BeautifulSoup(file,"lxml")
        soup.find(id="pokedex")

        for tab in  soup.find_all("tr"):
         for data in tab.find_all("td"):
             print(data.text)
             print("\n")

















print("coucou ")