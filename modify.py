#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: modify.py
@created: 08/02/2024
@updated 14/02/2024

@project: myDiscord
@licence: GPLv3
"""

"""Ce fichier est appelé par les boutons des interfaces graphiques.
Il appelle à son tour, soit le module message.py, soit user.py, soit channel.py
Ces modules utilise leur méthodes propres (avec du sql) et font appel a db.py"""

from message import Message
# from channel import Channel
from user import User
from db import Db


""" récupère les messages et les channels depuis la BDD"""
user_name = "user_name"
current_channel = "current_channel"
db = Db()
db.connect()
messages = db.query("SELECT content FROM message")
channels_list = db.query("SELECT channel_name, creator_name FROM rooms")
# print(channels_list)
channels = {}
for channel_name, user_name in channels_list:
    if channel_name not in channels:
        channels[channel_name] = [user_name]
    else:
        channels[channel_name].append(user_name)

class Modify:
    def __init__(self):
        self.message = Message()
        # self.channel = Channel()
        self.user = User()
        self.db = Db()

    def createMessage(self, user_name, channel_name, content):
        if channel_name not in channels:
            print("Veuillez choisir un channel existant.")
            return
        self.message.create(user_name, channel_name, content)


    def updateMessage(self, id, id_channel):
        try:
            id = int(id)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.message.update(id, id_channel)


    def deleteMessage(self, id_message):
        """Supprime un message avec l'ID spécifié"""
        try:
            id_message = int(id_message)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.message.delete(id_message)

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

    def createChannel(self, current_user, creator_id, channel_name):
        # Extraire les noms des channels de la liste
        channels = [channel[0] for channel in channels_list]

        if channel_name in channels:
            print("Ce channel existe déjà. Veuillez choisir un autre nom.")
            return
        self.create(creator_id, channel_name)
        print(f"Création du channel : {channel_name} par l'utilisateur {current_user}, id : {creator_id[0]}. Bravo Bruno, ce n'était pas facile !")







    def updateChannel(self, id, id_channel):
        try:
            id = int(id)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.channel.update(id, id_channel)


    def deleteChannel(self):
        """Supprime un message avec l'ID spécifié"""
        id_channel = input("ID de la channel : ")

        try:
            id_channel = int(id)
        except ValueError:
            print("L'ID de message est invalide. Veuillez entrer un nombre.")
            return

        self.channel.delete(id_channel)
    

    def findChannel(self):
        id_channel = input("ID du channel : ")

        try:
            id_channel = int(id_channel)
        except ValueError:
            print("ID de categorie invalide. Veuillez entrer un nombre.")
            # self.menu()

        print(self.channel.find(id_channel))
        # self.menu()

    def addMessageToChannel(self):
        id_message = input("ID du message : ")
        id_channel = input("ID de la channel : ")

        try:
            id_message = int(id_message)
            id_channel = int(id_channel)
        except ValueError:
            print("ID de message ou ID de channel invalide. Veuillez entrer un nombre.")

        self.channel.addMessage(id_message, id_channel)
