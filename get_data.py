
#/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: get_data.py
@created: 15/02/2024

@project: myDiscord 
@licence: GPLv3
"""
"""le fichier get_data crée les variables 'messages et 'channels', elles sont appelées par gui_message pour y être affiché"""
import mariadb
from db import Db
from modify import Modify
modify = Modify()
db = Db()


def fetch_messages_from_db(conn):
    messages = []
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT content FROM message")
        for (content,) in cursor:
            messages.append(content)
    except mariadb.Error as e:
        print(f"Erreur lors de la récupération des messages : {e}")
    finally:
        cursor.close()
    return messages


def fetch_channels_and_users_from_db(conn):
    channels = {}
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT channel_name, user_name FROM channel_user")
        for (channel_name, user_name) in cursor:
            if channel_name not in channels:
                channels[channel_name] = [user_name]
            else:
                channels[channel_name].append(user_name)
    except mariadb.Error as e:
        print(f"Erreur lors de la récupération des canaux et des utilisateurs : {e}")
    finally:
        cursor.close()
    return channels


""" récupère les messages et les channels depuis la BDD"""

current_channel = "current_channel"

# user_name = "user_name"


messages = db.query("SELECT content FROM message")
channels_list = db.query("SELECT channel_name, creator_name FROM channel")
# print(channels_list)
channels = {}
for channel_name, user_name in channels_list:
    if channel_name not in channels:
        channels[channel_name] = [user_name]
    else:
        channels[channel_name].append(user_name)




def main():

    db = Db()
    
    conn=db.__connect()


    if conn:
        messages = fetch_messages_from_db(conn)
        channels = fetch_channels_and_users_from_db(conn)
        print("Messages récupérés depuis la base de données :", messages)
        print("Canaux et utilisateurs récupérés depuis la base de données :", channels)
        conn.close()

if __name__ == "__main__":
    main()
