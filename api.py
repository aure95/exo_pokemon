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
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
    cursor = conn.cursor()
    cursor.execute(requete)
    reponse=cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return reponse



@hug.get('/PUT/pokemon')
def happy_birthday():
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
    cursor = conn.cursor()
    envoyerRequete("INSERT INTO `assoc_pokemon_type`(`id_pokemon`, `id_type`) VALUES ('1','1')")
    conn.commit()
    cursor.close()
    conn.close()
    """Says happy birthday to pokemon"""
    return "INSERT INTO `assoc_pokemon_type`(`id_pokemon`, `id_type`) VALUES ('1','1')"

@hug.get('/GET/pokemon')
def pokemon(id :hug.types.number):
    conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
    cursor = conn.cursor()
    reponse=envoyerRequeteReponse("SELECT * FROM `pokemon` WHERE id="+str(id))
    conn.commit()
    cursor.close()
    conn.close()
    """Says happy birthday to pokemon"""
    return reponse

@hug.get('/GET/all_pokemon')
def all_pokemon():

    liste=[]

    conn = mysql.connector.connect(host="localhost", user="root", password="", database="db_pokemon")
    cursor = conn.cursor()
    reponse=envoyerRequeteReponse("SELECT * FROM `pokemon` WHERE 1")
    conn.commit()
    cursor.close()
    conn.close()

    for data in reponse:
        liste.append(data)
    """Says happy birthday to pokemon"""
    return str(liste)