#/usr/bin/python3

import hug

from bs4 import BeautifulSoup

CONST_TAILLE_PARSE=9

#/////////////////////////////////////////////////////////////////////////

def splitPokemonType(pokemon):

    type=[]
    pos=""
    print(pokemon.getData()[1])
    taille_lim=len(pokemon.getData()[1])
    cpt=0


    for i in range(len(pokemon.getData()[1])):
      if pokemon.getData()[1][i].isupper():

      #    print(pokemon.getData()[1][i])

          #liste.append(pokemon.getData()[1][i])
          pos+=str(i)
          cpt+=1
    if cpt>=2:

        for i in range(len(pos)):

            if(len(pos)-i-1)!=0:

                if i < len(pos):
    #                print(i)
                    type.append(pokemon.getData()[1][int(pos[i]):int(pos[(i+1)])])
            else:
                #type.append(pokemon.getData()[1][int(pos[i]):int(pos[len(pos)])])
                type.append(pokemon.getData()[1][int(pos[i]):taille_lim])

    else:
        type.append(pokemon.getData()[1])

    return type


def splitType(chaine):

    type=[]
    pos=""
  #  print(chaine)
    taille_lim=len(chaine)
    cpt=0


    for i in range(len(chaine)):
      if chaine[i].isupper():

      #    print(pokemon.getData()[1][i])

          #liste.append(pokemon.getData()[1][i])
          pos+=str(i)
          cpt+=1
    if cpt>=2:

        for i in range(len(pos)):

            if(len(pos)-i-1)!=0:

                if i < len(pos):
    #                print(i)
                    type.append(chaine[int(pos[i]):int(pos[(i+1)])])
            else:
                #type.append(pokemon.getData()[1][int(pos[i]):int(pos[len(pos)])])
                type.append(chaine[int(pos[i]):taille_lim])

    else:
        type.append(chaine)

    return type


#////////////////////////////////////////////////////////////////////
class Pokemon:

    def __init__(self,name,type_no_splited,total,attack,defense,sp_attack,sp_defense,speed):

        self.CONVERTED=False
        self.type_splitted =[]
        self.name = name
        self.type_no_splitted = type_no_splited
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
        data.append(self.type_no_splitted)
        data.append(self.total)
        data.append(self.attack)
        data.append(self.defense)
        data.append(self.sp_attack)
        data.append(self.sp_defense)
        data.append(self.speed)

        return data

    def setTypeSplited(self,listeType):

        self.type_no_splitted=listeType
        self.CONVERTED=True


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
#////////////////////////////FUNCTION/////////////////////////////////










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


    #    print("/////////////"+str(cpt_pokemon)+"/////////////////")

        for data in tab.find_all("td"):


            if (cpt_parser!= 0):
                if cpt >0:
                    if cpt<CONST_TAILLE_PARSE:

             #           print(data.text+" "+str(cpt_parser))
                        liste.append(data.text)
    #                    print("len liste = %i  cpt_parser= %i"%(len(liste),cpt_parser))




                        if cpt>CONST_TAILLE_PARSE:
                            cpt=0




                    else:

                        print("cpt_pokemon = %i\n" % (cpt_pokemon))


        #              pokemon_data = Pokemon(liste[0],liste[1],liste[2],liste[3],liste[4],liste[5],liste[6],liste[7])
         #               print(pokemon_data.getData())
         #               listePokemon.append(pokemon_data)
                        #cpt=0
                    #else:
                        # cpt_parser+=1
                else:
                    cpt+=1
            cpt_parser += 1


      #  print(liste)


     #?
        if cpt_pokemon !=1:

             pokemon_data = Pokemon(liste[0], liste[1], liste[2], liste[3], liste[4], liste[5], liste[6], liste[7])

        #     print(pokemon_data.getData())
             listePokemon.append(pokemon_data)


print("\ncpt_pokemon = %i\n"%(cpt_pokemon))

'''
for pokemon in listePokemon:
    print(splitPokemonType(pokemon))

'''

'''
for data in listePokemon:
    print(data.getData())
    print("\n")
'''
print("\n///////////////////////////\n")

for data in listePokemon:
    print(data.getData())
    print("\n")






