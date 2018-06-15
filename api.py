#/usr/bin/python3
# coding: utf8

import hug
import mysql.connector

def envoyerRequete(requete):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
    cursor = conn.cursor()
    cursor.execute(requete)
    conn.commit()
    cursor.close()
    conn.close()

def envoyerRequeteReponse(requete):
    reponse=[]
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
    cursor = conn.cursor()
    cursor.execute(requete)

    for data in cursor:
        reponse.append(data)


    conn.commit()
    cursor.close()
    conn.close()
    return reponse


'''
@hug.get('/PUT/pokemon')
def happy_birthday(name:hug.type.text,type_id:hug.type.text,total:hug.type.number,hp:hug.type.text,attack:hug.type.number,defense:type.number,sp_atk:hug.type.number,sp_def:hug.type.number):
    
   # reponse=envoyerRequeteReponse()

    #envoyerRequete("INSERT INTO `pokemon`( `name`, `type_id`, `total`, `hp`, `attack`, `defense`, `sp_atk`, `sp_def`) VALUES ("+"'"+name+"''",)")
    
    """Says happy birthday to pokemon"""

    return "INSERT INTO `assoc_pokemon_type`(`id_pokemon`, `id_type`) VALUES ('1','1')"
'''

@hug.get('/GET/pokemon')
def pokemon(id :hug.types.number):

    reponse=""

    rep=envoyerRequeteReponse("SELECT * FROM `pokemon` WHERE id="+str(id))

    for r in rep:
        reponse+=str(rep)

    """Says happy birthday to pokemon"""
    return reponse

@hug.get('/GET/all_pokemon')
def all_pokemon():

    liste=[]
    reponse=envoyerRequeteReponse("SELECT * FROM `pokemon` WHERE 1")


    for data in reponse:
        liste.append(data)
    """Says happy birthday to pokemon"""
    return str(liste)