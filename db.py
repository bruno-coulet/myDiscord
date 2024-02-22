
#/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: db.py
@created: 08/02/2024

@project: myDiscord 
@licence: GPLv3
"""
from dotenv import load_dotenv
import os
import mariadb


load_dotenv()


class Db:
    def __init__(self):
        self.__url = os.getenv('DB_HOST')
        self.__user = os.getenv('DB_USER')
        self.__pw = os.getenv('DB_PASSWORD')
        self.__port = int(os.getenv('DB_PORT'))
        self.__database = os.getenv('DB_NAME')

    def __connect(self):
        # Connexion à la BDD
        base = mariadb.connect(
                host=self.__url,
                user=self.__user,
                password=self.__pw,
                port=self.__port,
                database=self.__database,
                autocommit=False
                )
        # Création de l'objet curseur
        cursor = base.cursor()
        return base, cursor

    def query(self, req, modif=False):
        base, cursor = self.__connect()
        # Exécute la requête SQL
        cursor.execute(req)
        base.commit()
        if modif is False:
            res = cursor.fetchall()
            return res
        # Fermeture de la connexion
        cursor.close()
        base.close()






if __name__ == '__main__':
    db = Db()
    print(db.query("SHOW TABLES"))
    print(db.query("SELECT name FROM user"))



