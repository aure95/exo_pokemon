#/usr/bin/python3

import hug

from bs4 import BeautifulSoup

#////////////////////////////////////////////////////////////////////
class Pokemon:

    '''
    #pass= permet de redefinir constructeur
    def __init__(self):

    pass
    '''



    def __init__(self):

        self.name = "ame"
        self.type = "type"
        self.total = "total"
        self.attack = "attack"
        self.defense = "defense"
        self.sp_attack = "sp_attack"
        self.sp_defense = "sp_defense"
        self.speed = "speed"

        pass

    def getData(self):
        data = []

        data.append(self.name)
        data.append(self.type)
        data.append(self.total)
        data.append(self.attack)
        data.append(self.defense)
        data.append(self.sp_attack)
        data.append(self.sp_defense)
        data.append(self.speed)






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
'''



#/////////////////////////////////////////////////////////////


    #pokemon=Pokemon()

    #print(pokemon.getData())

with open("pokemon.html") as file:
    soup = BeautifulSoup(file,"lxml")
    soup.find(id="pokedex")

    for tab in  soup.find_all("tr"):
        for data in tab.find_all("td"):
             print(data.text)
             print("\n")

pokemon=Pokemon()
print("hola")
print(pokemon.name)
print("como esta")