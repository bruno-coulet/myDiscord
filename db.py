#!/usr/bin/venv python3
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
    """
    Class to manage DB operations
    """
    def __init__(self):
        self.__url = os.getenv('DB_HOST')
        self.__user = os.getenv('DB_USER')
        self.__pw = os.getenv('DB_PASSWORD')
        self.__port = int(os.getenv('DB_PORT'))
        self.__database = os.getenv('DB_NAME')
        self.base = None
        self.cursor = None

    def connect(self):
        """
        Connect to the database
        :return: None
        """
        try:
            self.base = mariadb.connect(
                    host=self.__url,
                    user=self.__user,
                    password=self.__pw,
                    port=self.__port,
                    database=self.__database,
                    autocommit=False
                    )
            self.cursor = self.base.cursor()
        except mariadb.Error as err:
            print(f"Error connecting to the database: {err}")

    def query(self, req, mod=False):
        """
        Query the database
        :param req: request sql injection string
        :param mod: False for read, True to create | update | delete
        :return: None | list
        """
        try:
            self.cursor.execute(req)
            if mod:
                self.base.commit()
            else:
                res = self.cursor.fetchall()
                return res
        except mariadb.Error as err:
            print(f"Error query: {err}")

    def disconnect(self):
        """
        Disconnect from the database
        :return: None
        """
        self.cursor.close()
        self.base.close()


if __name__ == '__main__':
    db = Db()
    db.connect()
    print(db.query("SHOW TABLES"))
    for k in range(10):
        print(k)
    print(db.query("SHOW DATABASES"))
    print(db.query("SHOW TABLES"))
    print(type(db.base), type(db.cursor))
    db.disconnect()
