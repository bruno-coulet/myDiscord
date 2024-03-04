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




   # def create(self, creator_id, channel_name):
   #      query = f'INSERT INTO {self.table}(user_name, channel_name) VALUES (\'{creator_id}\', \'{channel_name}\')'
   #      self.db.query(query, modif=True)
       
   def create(self, creator_id, channel_name):
      # Récupérer les informations de l'utilisateur à partir de son ID
      user_query = f'SELECT first_name, name FROM users WHERE id = {creator_id}'
      user_result = self.db.query(user_query)

      if user_result:
         # Extraire les informations de l'utilisateur
         first_name = user_result[0][0]
         name = user_result[0][1]

         # Construire la requête d'insertion en utilisant les informations de l'utilisateur
         query = f"INSERT INTO {self.table}(channel_name, creator_name) VALUES ('{channel_name}', '{first_name} {name}')"
         self.db.query(query, modif=True)
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
