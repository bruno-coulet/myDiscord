#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: channel.py
@created: 08/02/2024
@updated 14/02/2024

@project: myDiscord
@licence: GPLv3
"""

from db import Db


class Channel:
    def __init__(self):
       self.table = 'channel'
       self.db = Db()



    # def create(self, name):
    #    query = f'INSERT INTO {self.table} (name) VALUES (%s)'
    #    params = (name, )
    #    self.db.executeQuery(query, params)

    def create(self, user_name, channel_name):
        query = f'INSERT INTO {self.table}(user_name, channel_name) VALUES (\'{user_name}\', \'{channel_name}\')'
        self.db.query(query, modif=True)


    def read(self):
       query = f'SELECT * FROM {self.table}'
       return self.db.fetch(query)


    def update(self, id, name):
       query = f'UPDATE {self.table} SET name=%s  WHERE id=%s'
       params = (name, id)
       self.db.executeQuery(query, params)


    def delete(self, id):
       query = f'DELETE FROM {self.table} WHERE id=%s'
       params = (id,)
       self.db.executeQuery(query, params)


    def find(self, id):
       query = f'SELECT * FROM {self.table} WHERE id=%s'
       params = (id,)
       return self.db.fetch(query, params)
