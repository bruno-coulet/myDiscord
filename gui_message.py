#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: button.py
@created: 11/02/2024

@project: myDiscord
@licence: GPLv3
"""

import customtkinter

def create_channel():
    print("create channel")

def send_message():
    print("send message")

def log_out():
    print("log out")

class Messagerie(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        self.title("Messagerie")
        self.geometry("600x700")
        # give both columns an equal weight.
        self.grid_columnconfigure((0, 1), weight=1)

        # Titre de la fenêtre
        title_label = customtkinter.CTkLabel(self, text="Bienvenue dans la messagerie", font=("Helvetica", 16))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        

        self.button_create_channel = customtkinter.CTkButton(self, text="Créer un channel", command=create_channel)
        self.button_create_channel.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # sticky="ew"  --->   occupe toute la largeur de la cellule
        self.button_send_message = customtkinter.CTkButton(self, text="Publier le message", command=lambda: print("send message", entry_text.get()))
        self.button_send_message.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # message text ou audio
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="Message texte")
        self.checkbox_1.grid(row=3, column=0, padx=20, pady=(20, 20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="Message audio")
        self.checkbox_2.grid(row=3, column=1, padx=20, pady=(20, 20), sticky="w")

        # Zone de saisie de texte
        entry_text = customtkinter.CTkEntry(self, width=400, height=100)
        entry_text.grid(row=4, column=0, padx=10, pady=10)

        # Label
        message_label = customtkinter.CTkLabel(self, text="Messages du channel.")
        message_label.grid(row=5, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.checkbox_frame = customtkinter.CTkFrame(self)
        self.checkbox_frame.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="nsw")
        self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="message 1")
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="message 2")
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")




        self.button_log_out = customtkinter.CTkButton(self, text="Se déconnecter", command=log_out)
        self.button_log_out.grid(row=7 , column=0, padx=20, pady=20, sticky="ew", columnspan=2)

        # column 0 spans the whole window because it has a weight of 1 and therefore expands.
        # donc cela centre le bouton car la colonne fait toute la largeur de la fenêtre
        # self.grid_columnconfigure(0, weight=1)

        # self.grid_rowconfigure(0, weight=1)


messagerie = Messagerie()
messagerie.mainloop()