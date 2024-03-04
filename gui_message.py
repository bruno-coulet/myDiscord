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
import tkinter.messagebox as tkmb
import sys
import os
import time

# from update import Update

db = Db()
modify=Modify()

""" récupère les DATA depuis la BDD"""
# liste de tuples, chacun contient un seul élément : le contenu d'un message.
messages = db.query("SELECT content FROM message")
# Charge le nom d'utilisateur passé en argument en ligne de commande sinon utilisateur inconnu
current_user = sys.argv[1] if len(sys.argv) > 1 else "Unknown User"
# Extrait le nom d'utilisateur à partir de l'argument en ligne de commande
current_user = current_user.strip()



""" affiche les messages existants   """   
class ScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.configure(fg_color=FG_SECOND_COLOR)

        for i, value in enumerate(self.values):
            message_content = value[0]  # Accéder au premier élément du tuple, sinon cela affiche les messages entre accolades
            label = ctk.CTkLabel(self, text=message_content, text_color=TEXT_COLOR)  # Couleur du texte pour chaque étiquette
            label.grid(row=i+1, column=0, padx=10, pady=(10, 0))

    def update_channel_messages(self, new_messages):
        # Efface tous les messages actuellement affichés
        for widget in self.winfo_children():
            widget.destroy()
        # Affiche les nouveaux messages
        for i, value in enumerate(new_messages):
            message_content = value[0]
            label = ctk.CTkLabel(self, text=message_content, text_color=TEXT_COLOR)
            label.grid(row=i+1, column=0, padx=10, pady=(10, 0))





class Message(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Messagerie")
        self.geometry("1200x700")
        self.grid_columnconfigure((0, 1), weight=1)
        self.configure(fg_color=FG_COLOR)


        # DATA POUR LE TREEVIEW
        channels_data = db.query("SELECT c.channel_name, u.firstname FROM channel c LEFT JOIN channel_user cu ON c.id = cu.channel_id LEFT JOIN users u ON cu.user_id = u.id")
        channels_user  = {}
        for channel_name, user_name in channels_data:  
            if channel_name not in channels_user :
                #  initialise une liste d'utilisateur associé au channel
                #  attribue cette liste à la clé channel_name.
                channels_user [channel_name] = [user_name]
            else:
                # ajoute l'utilisateur au channel existant
                channels_user [channel_name].append(user_name)
        print(f'nom du channel actuel : {channel_name}')


        # Définir l'attribut self.current_channel_name
        self.current_channel_name = None
        # Définir l'attribut self.current_channel
        self.current_channel = None


        title_label = ctk.CTkLabel(self, text=f"Bienvenue dans la messagerie {current_user}", font=(TITLE_FONT), text_color=TEXT_COLOR)
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        title_label.pack_propagate(False)

        def log_out():
            print("log out")
            self.destroy()  # Détruit la fenêtre actuelle
            os.system("python login.py")

        self.button_log_out = ctk.CTkButton(self, text="Se déconnecter", text_color=TEXT_COLOR, command=log_out)
        self.button_log_out.grid(row=0 , column=2, padx=20, pady=20)


        self.channel_frame = ctk.CTkFrame(self)
        self.channel_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ns", rowspan=4)
        self.channel_frame.grid_columnconfigure((0, 1), weight=1)
        self.channel_frame.configure(fg_color=FG_COLOR, border_width=2, border_color=BORDER_COLOR)


        self.current_channel_frame = ctk.CTkFrame(self.channel_frame)
        self.current_channel_frame.grid(row=0, column=0, padx=10, pady=(10, 0))
        self.current_channel_frame.configure(fg_color=FG_SECOND_COLOR)

        current_channel_label = ctk.CTkLabel(self.current_channel_frame, text=f"Channel actuel : {channel_name}", font=SUBTITLE_FONT, text_color=TEXT_COLOR)
        current_channel_label.grid(row=0, column=0, padx=20, pady=20)

        current_channel_title = ctk.CTkLabel(self.current_channel_frame, font=FONT, wraplength=200)
        current_channel_title.grid(row=1, column=0, padx=20, pady=20)


        self.channel_tree = ttk.Treeview(self.current_channel_frame)
        self.channel_tree.heading("#0", text="Autre channels")
        self.channel_tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", rowspan=3)


        # Gestionnaire d'événements pour le TreeView
        def select_channel(event):
            selected_item = self.channel_tree.selection()
            if selected_item:
                self.current_channel = self.channel_tree.item(selected_item, "text")
                # Met à jour les messages en fonction du channel
                sort_messages(self.current_channel)
                # Met à jour le nom du channel en fonction du channel sélectionné
                current_channel_label.configure(text=f"Channel actuel : {self.current_channel}")
                print(f"channel sélectionné : {self.current_channel}")




        # Met à jour les messages en fonction du channel
        def sort_messages(channel_name):
            messages = db.query(f"SELECT content FROM message WHERE channel_name = '{channel_name}'")
            self.old_message_frame.update_channel_messages(messages)







        # Associez le gestionnaire d'événements au TreeView
        self.channel_tree.bind("<<TreeviewSelect>>", select_channel)
        # Ajouter des canaux au treeview
        for channel_name, users in channels_user.items():
            self.channel_tree.insert("", "end", text=channel_name)
        

        # ----  CHANNEL / CREATE    ROW 1.5  COL 0
        def create_channel():
            new_channel_name = channel_entry_text.get()  # Récupère le texte entré dans entry_text
            # Recherche de l'user_id du créateur dans la base de données
            creator_id_query = f"SELECT id FROM users WHERE nickname = '{current_user}'"
            result = db.query(creator_id_query)  # Utilise query pour obtenir un seul résultat
            print(f"current_user : {current_user}")

            if result:
                creator_id = result[0]  # Si un résultat est trouvé, récupère l'user_id
                print(f"creator_id : {creator_id[0]}")
                modify.createChannel(current_user, creator_id=creator_id, channel_name=new_channel_name)
                tkmb.showinfo(title="Channel Created", message="Channel created successfully")
            else:
                tkmb.showerror(title="Error", message="User not found")



        
        new_channel_label = ctk.CTkLabel(self.channel_frame, text="Créez un channel :", font=SUBTITLE_FONT, text_color=TEXT_COLOR)
        new_channel_label.grid(row=3, column=0, padx=10, pady=10)
        # --------  input area
        channel_entry_text = ctk.CTkEntry(self.channel_frame)
        channel_entry_text.grid(row=4, column=0, padx=10, pady=10)
        channel_entry_text.configure(fg_color=FG_COLOR, border_width=2, border_color=BORDER_COLOR, text_color=TEXT_COLOR)
        # -------- create channel button---------------------------------------------------------------------------------
        self.button_create_channel = ctk.CTkButton(self.channel_frame, text="Valider le channel", text_color=TEXT_COLOR, command=create_channel)
        self.button_create_channel.grid(row=5, column=0, padx=20, pady=20, sticky="s")



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
        new_message_label = ctk.CTkLabel(self.message_frame, text="Nouveau Message.", text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        new_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        # -------- is text  -   ROW 3.1    COL 0    ---
        self.checkbox_text_message = ctk.CTkCheckBox(self.message_frame, text="Message texte", text_color=TEXT_COLOR)
        self.checkbox_text_message.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="w")
        # -------- is audio  -  ROW 3.1    COL 1    ---
        self.checkbox_audio_message = ctk.CTkCheckBox(self.message_frame, text="Message audio", text_color=TEXT_COLOR)
        self.checkbox_audio_message.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="w")
        # --------  input area
        entry_text = ctk.CTkEntry(self.message_frame, width=600, height=50,)
        entry_text.grid(row=2, column=0, padx=10, pady=10)
        entry_text.configure(fg_color=FG_COLOR, border_width=2, border_color=BORDER_COLOR, text_color=TEXT_COLOR)

        # -------- send message button---------------------------------------------------------------------------------
        def send_message():
            req = "SELECT channel.channel_name, message.channel_name FROM `channel`, `message` WHERE message.channel_name = channel.channel_name LIMIT 0,50;"
            modify.createMessage(user_name=current_user, channel_name=self.current_channel, content=entry_text.get())
            print("Message envoyé:", entry_text.get())
            print(f"dans le channnel: {self.current_channel}")



        

        self.button_send_message = ctk.CTkButton(self.message_frame, text="Publier le message", text_color=TEXT_COLOR, command=lambda: send_message())
        self.button_send_message.grid(row=3, column=0, padx=20, pady=20)



if __name__ == "__main__":
    gui_message = Message()
    gui_message.mainloop()