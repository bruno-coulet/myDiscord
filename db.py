
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
        self.__url = os.getenv('url')
        self.__user = os.getenv('user')
        self.__pw = os.getenv('pw')
        self.__port = int(os.getenv('port'))
        self.__database = os.getenv('db')

    def __connect(self):
        base = mariadb.connect(
                host=self.__url,
                user=self.__user,
                password=self.__pw,
                port=self.__port,
                database=self.__database,
                autocommit=False
                )
        cursor = base.cursor()
        return base, cursor

    def query(self, req, modif=False):
        base, cursor = self.__connect()
        cursor.execute(req)
        base.commit()
        if modif is False:
            res = cursor.fetchall()
            return res
        cursor.close()
        base.close()

    # def query(self, req, values=None, modif=False):
    #     base, cursor = self.__connect()
    #     cursor.execute(req, values)  # Execute the query with parameters
    #     base.commit()
    #     if modif is False:
    #         res = cursor.fetchall()
    #         cursor.close()
    #         base.close()
    #         return res
    #     cursor.close()
    #     base.close()






if __name__ == '__main__':
    db = Db()
    print(db.query("SHOW TABLES"))

