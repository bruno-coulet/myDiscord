
#/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: db.py
@created: 15/02/2024

@project: myDiscord 
@licence: GPLv3
"""

import mariadb
from db import Db

def fetch_messages_from_database(conn):
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

# Récupérez les canaux et les utilisateurs depuis la base de données
def fetch_channels_and_users_from_database(conn):
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

# Exemple d'utilisation
def main():

    db = Db()
    
    conn=db.connect()


    if conn:
        messages = fetch_messages_from_database(conn)
        channels = fetch_channels_and_users_from_database(conn)
        print("Messages récupérés depuis la base de données :", messages)
        print("Canaux et utilisateurs récupérés depuis la base de données :", channels)
        conn.close()

if __name__ == "__main__":
    main()
