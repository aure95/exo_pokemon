#/usr/bin/python3

import hug

from bs4 import BeautifulSoup

CONST_TAILLE_PARSE=9


#////////////////////////////////////////////////////////////////////
class Pokemon:

    def __init__(self,name,type,total,attack,defense,sp_attack,sp_defense,speed):

        self.name = name
        self.type = type
        self.total = total
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed

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
    #pass= permet de redefinir constructeur
    def __init__(self):

    pass
    '''


'''
    def __init__(self):

        self.name = "name"
        self.type = "type"
        self.total = "total"
        self.attack = "attack"
        self.defense = "defense"
        self.sp_attack = "sp_attack"
        self.sp_defense = "sp_defense"
        self.speed = "speed"

        pass
'''







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

listePokemon=[]
liste=[]
cpt=0
cpt_pokemon=0
cpt_parser=0





with open("pokemon.html") as file:
    soup = BeautifulSoup(file,"lxml")
    soup.find(id="pokedex")

    for tab in soup.find_all("tr"):
        liste=[]
        cpt_pokemon += 1
        cpt_parser = 0


        print("/////////////"+str(cpt_pokemon)+"/////////////////")

        for data in tab.find_all("td"):


            if (cpt_parser!= 0):
                if cpt >0:
                    if cpt<CONST_TAILLE_PARSE:

                        print(data.text+" "+str(cpt_parser))
                        liste.append(data.text)


                        if cpt>CONST_TAILLE_PARSE:
                            cpt=0



                    else:
                        print("hola")
                        #print("cpt_pokemon = %i\n" % (cpt_pokemon))
              #          pokemon_data = Pokemon(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7])
                        #print(pokemon_data.getData())
               #         listePokemon.append(pokemon_data)
                        #cpt=0
                    #else:
                        # cpt_parser+=1
                else:
                    cpt+=1
            cpt_parser += 1


print("cpt_pokemon = %i"%(cpt_pokemon))


'''
for data in listePokemon:
    print(data.getData())
    print("\n")
'''