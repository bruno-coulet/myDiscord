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

       
   def create(self, creator_id, channel_name):
      user_query = f'SELECT firstname, lastname FROM users WHERE id = {creator_id}'
      user_result = self.db.query(user_query)

      if user_result:
        firstname = user_result[0][0]
        lastname = user_result[0][1]
        query = f"INSERT INTO {self.table}(channel_name, creator_name) VALUES (%s, %s)"
        params = (channel_name, f"{firstname} {lastname}")
        print("Query:", query)
        print("Params:", params)

        self.db.query(query, params=params, modif=True)

      else:
         print("Utilisateur non trouvé.")




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
