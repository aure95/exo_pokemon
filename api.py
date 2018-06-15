#/usr/bin/python3
# coding: utf8

import hug

from bs4 import BeautifulSoup
import mysql.connector

TABLE_TRUNCATE=("type","pokemon","assoc_pokemon_type")

INSERTION_POKEMON_TYPE=True

CONST_TAILLE_PARSE=9

CONST_REQUETE_SELECT_POK_TYPE_VOID="SELECT count(*) FROM `type` WHERE 1 "

CONST_LISTE_TYPE_POK=("Normal","Fire","Water","Electric","Grass","Ice","Fighting","Poison","Ground","Flying","Psychic","Bug","Rock","Ghost","Dragon","Dark","Steel","Fairy")


#//////////////////////////////CONST REQUETE///////////////////////////////////////////////////////////////

CONST_REQUETE_INSERT_POK_TYPE=("INSERT INTO `type`(`name`) VALUES (",");")

CONST_REQUETE_INSERTION_POKEMON=("INSERT INTO `pokemon`(`name`, `total`, `hp`, `attack`, `defense`, `sp_atk`, `sp_def`) VALUES (",");")
CONST_REQUETE_INSERTION_POKEMON=("INSERT INTO `pokemon`(`name`, `type_id`, `total`, `hp`, `attack`, `defense`, `sp_atk`, `sp_def`) VALUES (",");")

#//////////////////////////////FUNCTION SQL///////////////////////////////////////////

conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
cursor = conn.cursor()

#   *plusieurs parametre possible

#https://stackoverflow.com/questions/15288594/update-database-with-multiple-sql-statments/15291171

def envoyerRequeteSQL(requete):

    print(requete)
    cursor.execute(requete)
    conn.commit()

def verifvoidTabletype():

    response=0

    cursor.execute(CONST_REQUETE_SELECT_POK_TYPE_VOID)
    conn.commit()
    response=int(cursor.fetchone())
    return(response)






def initialisionDBSQl():

    #file=open("db_pokemon_config.txt","r")
    #instructions="drop database if exists db_pokemon;create database db_pokemon;create table type(  id integer primary key AUTO_INCREMENT not null,name varchar(10) not null unique   );create table pokemon( id int PRIMARY KEY not null AUTO_INCREMENT,name varchar(50) not null unique,type_id integer not null,total int(10) not null,hp int(10) not null,attack int(10) not null,defense int(10) not null,sp_atk int(10) not null,sp_def int(10) not null,speed  int(10) not null);ALTER TABLE pokemon ENGINE=InnoDB;ALTER TABLE type ENGINE=InnoDB;ALTER TABLE pokemon ADD CONSTRAINT fk_type_name FOREIGN KEY (type_id) REFERENCES type(id);"

    cpt=0


    #parcours le fichier

    #envoyerRequeteSQL(instructions.encode('utf8'))

    #file.close()
    print("\n//////////////INITIAILISATION DB OK////////////////\n")

def fermerConnexionSQL():

    cursor.close()
    conn.close()


#////////////////////////////////////////////////////////////////////
def truncateTable():

    cursor.execute("SET FOREIGN_KEY_CHECKS=0")
    for i in range(len(TABLE_TRUNCATE)):
        cursor.execute("TRUNCATE TABLE "+TABLE_TRUNCATE[i])

    cursor.execute("SET FOREIGN_KEY_CHECKS=1")
    conn.commit()

    print("TABLE TRUNCATED "+str(TABLE_TRUNCATE))

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



def chercherIndexAttack(data_type):

    index=[]
    list_data=list(CONST_LISTE_TYPE_POK)

    for data in data_type:

        if data_type[0] in list_data:
            index.append(list_data.index(data)+1)

    return index







def insertionPokemonTypeMySQL():


    #print(CONST_REQUETE_INSERT_POK_TYPE)
    for type in CONST_LISTE_TYPE_POK:
        # print(type)
       #print(CONST_REQUETE_INSERT_POK_TYPE[0]+"'"+type+"'"+CONST_REQUETE_INSERT_POK_TYPE[1])
       envoyerRequeteSQL(CONST_REQUETE_INSERT_POK_TYPE[0]+"'"+type+"'"+CONST_REQUETE_INSERT_POK_TYPE[1])

    print("//////////TYPE POKEMON INSERTED//////////")

def insertionPokemonMySQL(listePokemon):

    requete="'"
    cpt=0
    cpt_bulbausaur=0

    #Bulbasaur hardcoded car pas present lors du parsing (probleme dans boucle)

    for pok in listePokemon:
       print(pok.getData())
       data=pok.getData()
       cpt=0
       requete = "'"


       '''
        # probleme avec "Farfetch'd"
       if pok.getData()[0]=="Farfetch'd":
           pokemon=Pokemon("Farfetchd",pok.getData()[1],pok.getData()[2],pok.getData()[3],pok.getData()[4],pok.getData()[5],pok.getData()[6],pok.getData()[7])
           pok=pokemon
       '''
       for caract in data:

            if cpt!=1:
                '''
                if cpt_bulbausaur == 0:
                    requete += "Bulbasaur','"
                    cpt_bulbausaur = 1
                else:
                '''
                if cpt==0:
                    caract=caract.replace("'"," ")
                    print(caract)
                if cpt==2:
                    '''
                    if cpt_bulbausaur == 0:
                        requete+="tamera"
                        cpt_bulbausaur = 1
                    else:
                        requete += str(pok.getIndex()[0])
                    '''
                    requete += str(pok.getIndex()[0])+"','"
                if cpt<len(pok.getData()):
                    requete+=caract+"',"
                    requete+="'"
            cpt+=1
       requete=requete[0:(len(requete)-2)]

      # print(requete)
      # print(CONST_REQUETE_INSERTION_POKEMON[0] + requete + CONST_REQUETE_INSERTION_POKEMON[1])
       envoyerRequeteSQL(CONST_REQUETE_INSERTION_POKEMON[0]+requete+CONST_REQUETE_INSERTION_POKEMON[1])





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
        self.index=[]
        self.type_no_splitted = type_no_splited

        self.setTypeSplited(splitType(self.type_no_splitted))

        self.index=chercherIndexAttack(self.type_splitted)
        self.total = total
        self.attack = attack
        self.defense = defense
        self.sp_attack = sp_attack
        self.sp_defense = sp_defense
        self.speed = speed


        pass

    def getIndex(self):

        return self.index

    def getData(self):

        data = []
        data.append(self.name)
    #
        data.append(self.type_splitted)
    #
        data.append(self.total)
        data.append(self.attack)
        data.append(self.defense)
        data.append(self.sp_attack)
        data.append(self.sp_defense)
        data.append(self.speed)

        return data

    def setTypeSplited(self,listeType):

        self.type_splitted=listeType
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

             print(pokemon_data.getData())
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

'''
for data in listePokemon:
    print(data.getData())
    print("\n")
'''




#///////////////INITialisation DB/////////////

#initialisionDBSQl()


#initialisionDBSQl()

#envoyerRequeteSQL("INSERT INTO `type`(`name`) VALUES ('kj');")
#envoyerRequeteSQL("INSERT INTO `type`(`name`) VALUES ('test');")


#print(verifvoidTabletype())

#if verifvoidTabletype()!=0:
 #   INSERTION_POKEMON_TYPE = False



#if INSERTION_POKEMON_TYPE:
truncateTable()
insertionPokemonTypeMySQL()

pokemeonBulbizaur=Pokemon("Bulbasaur",'GrassPoison','318', '45', '49', '49', '65', '65')

listePokemon[0]=pokemeonBulbizaur

insertionPokemonMySQL(listePokemon)

for pok in listePokemon:
    print(pok.getIndex())



fermerConnexionSQL()







