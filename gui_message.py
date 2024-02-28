#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: gui_message.py
@created: 11/02/2024

@project: myDiscord
@licence: GPLv3
"""
"""                       SCHEMA DE POSITIONNEMENT
            COLUMN 0            COLUMN 1        COLUMN 2

ROW 0       TITLE,              TITLE,          logout button
ROW 1       CHANNEL title,      OLD MESSAGE,    OLD MESSAGE
ROW 2       CHANNEL treeview,   OLD MESSAGE,    OLD MESSAGE
ROW 3       CHANNEL treeview,   NEW MESSAGE,    NEW MESSAGE
ROW 4       CHANNEL treeview,   NEW MESSAGE,    NEW MESSAGE
ROW 5       CHANNEL select,     NEW MESSAGE,    send button

"""

import customtkinter as ctk
from constants import *
from tkinter import ttk
from modify import Modify
from db import Db
import sys
import os

# from update import Update

db = Db()
modify=Modify()

""" récupère les DATA depuis la BDD"""
messages = db.query("SELECT content FROM message")
channel = db.query("SELECT channel_name FROM channel WHERE ID=1")
channel_name=f"{channel[0][0]}"
users = db.query("SELECT lastname, firstname, ID FROM users WHERE ID=1")
user_first_name_and_name=f"{users[0][1]} {users[0][0]}"
user_first_name=f'{users[0][1]}'
user_id=f'{users[0][2]}'
# DATA POUR LE TREEVIEW
channels_data = db.query("SELECT c.id, c.channel_name, u.firstname FROM channel c JOIN channel_user cu ON c.id = cu.channel_id JOIN users u ON cu.user_id = u.id")
channels_user  = {}
for channel_id, channel_name, user_name in channels_data:  
    if channel_name not in channels_user :
        #  initialise une liste d'utilisateur associé au channel
        #  attribue cette liste à la clé channel_name.
        channels_user [channel_name] = [user_name]
    else:
        # ajoute l'utilisateur actuel à la liste existante d'utilisateurs
        channels_user [channel_name].append(user_name)
print(f'nom du channel : {channel_name}')
# print(f'prénom et nom de l\'utilisateur : {user_first_name_and_name}')
# print(f'id de l\'utilisateur : {user_id}')



# Charge le nom d'utilisateur passé en argument en ligne de commande
current_user = sys.argv[1] if len(sys.argv) > 1 else "Unknown User"

# Extrait le nom d'utilisateur à partir de l'argument en ligne de commande
current_user = current_user.strip()

# Récupère les données depuis la BDD
# messages = []  # Modifier pour récupérer les messages depuis la BDD
# channel_name = "General"  # Modifier pour récupérer le nom du canal depuis la BDD






# SERVIRA PEUT ETRE UN JOUR CHOISIR LE MODE AUDIO
def checkbox_callback(self):
    print("checked checkboxes:")

# SERVIRA PEUT ETRE UN JOUR CHOISIR LE MODE AUDIO
# def checkbox_callback(self):
#         print("checked checkboxes:")

#     # def get(self):
#     #     checked_checkboxes = []
#     #     for checkbox in self.checkboxes:
#     #         if checkbox.get() == 1:
#     #             checked_checkboxes.append(checkbox.cget("text"))
#     #     return checked_checkboxes 





""" affiche les messages existants   """   
class ScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.configure(fg_color=FG_SECOND_COLOR)
        # self.checkboxes = []

        for i, value in enumerate(self.values):
            label = ctk.CTkLabel(self, text=value)
            label.grid(row=i+1, column=0, padx=10, pady=(10, 0))



class Message(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Messagerie")
        self.geometry("1200x700")
        self.grid_columnconfigure((0, 1), weight=1)
        self.configure(fg_color=FG_COLOR)

        # ----  TITLE -             ROW 0     -------
        title_label = ctk.CTkLabel(self, text=f"Bienvenue dans la messagerie {current_user}", font=(TITLE_FONT))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        title_label.pack_propagate(False)

        # ----  LOGOUT       -      ROW 0 COL 2   ---
        def log_out():
            print("log out")
            self.destroy()  # Détruit la fenêtre actuelle
            os.system("python login.py")

        self.button_log_out = ctk.CTkButton(self, text="Se déconnecter", command=log_out)
        self.button_log_out.grid(row=0 , column=2, padx=20, pady=20)

        # ----  CHANNEL -           ROW 1,2,3,4   COL 0   -------
        self.channel_frame = ctk.CTkFrame(self)
        self.channel_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ns", rowspan=4)
        self.channel_frame.grid_columnconfigure((0, 1), weight=1)
        self.channel_frame.configure(fg_color=FG_COLOR, border_width=2, border_color=BORDER_COLOR)

        # ----  CHANNEL / CURRENT - ROW 1.0  COL 0   ---
        self.current_channel_frame = ctk.CTkFrame(self.channel_frame)
        self.current_channel_frame.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.current_channel_frame.configure(fg_color=FG_SECOND_COLOR)
        # title label               ROW 1.0.0    COL 0
        current_channel_label = ctk.CTkLabel(self.current_channel_frame, text=f"Channel actuel : {channel_name}", font=SUBTITLE_FONT)
        current_channel_label.grid(row=0, column=0, padx=20, pady=20)
        # title value               ROW 1.0.1    COL 0
        current_channel_title = ctk.CTkLabel(self.current_channel_frame, font=FONT, wraplength=200)
        current_channel_title.grid(row=1, column=0, padx=20, pady=20)

        # ----  CHANNEL / TREEVIEW  -  ROW 1.1 and 1.3    COL 0
        # Création du Treeview pour afficher les channels
        self.channel_tree = ttk.Treeview(self.current_channel_frame)
        self.channel_tree.heading("#0", text="Autre channels")
        self.channel_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=3)

        # ----  OLD MESSAGES FRAME -  ROW 1 and 2  COL 1 and 2
        self.old_message_frame = ScrollableFrame(self, values=[message for message in messages])
        self.old_message_frame.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="ew", columnspan=2, rowspan=2)
        self.old_message_frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        self.old_message_frame.pack_propagate(False)

        # ----  NEW MESSAGE FRAME  - ROW 3    COL 1 and 2    ---
        self.message_frame = ctk.CTkFrame(self)
        self.message_frame.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="ew", columnspan=2, rowspan=2)
        self.message_frame.grid_columnconfigure((0, 1), weight=1)
        self.message_frame.grid_rowconfigure((0, 1), weight=1)
        self.message_frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)

        # -------- label  -     ROW 3.0    COL 0 and 1    ---
        new_message_label = ctk.CTkLabel(self.message_frame, text="Nouveau Message.", font=SUBTITLE_FONT)
        new_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        # -------- is text  -   ROW 3.1    COL 0    ---
        self.checkbox_text_message = ctk.CTkCheckBox(self.message_frame, text="Message texte")
        self.checkbox_text_message.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="w")
        # -------- is audio  -  ROW 3.1    COL 1    ---
        self.checkbox_audio_message = ctk.CTkCheckBox(self.message_frame, text="Message audio")
        self.checkbox_audio_message.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="w")
        # --------  input area
        entry_text = ctk.CTkEntry(self.message_frame, width=600, height=50,)
        entry_text.grid(row=2, column=0, padx=10, pady=10)
        entry_text.configure(fg_color=FG_COLOR, border_width=2, border_color=BORDER_COLOR)

        # -------- send message button---------------------------------------------------------------------------------
        def send_message():
            req = f"SELECT channel.channel_name, message.channel_name FROM `channel`, `message` WHERE message.channel_name = channel.channel_name LIMIT 0,50;"
            modify.createMessage(user_name=current_user, channel_name=channel_name, content=entry_text.get())
            print("send message : ", entry_text.get())

        self.button_send_message = ctk.CTkButton(self.message_frame, text="Publier le message", command=lambda: send_message())
        self.button_send_message.grid(row=3, column=0, padx=20, pady=20)

if __name__ == "__main__":
    gui_message = Message()
    gui_message.mainloop()