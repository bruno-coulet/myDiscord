#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Lucas SAVIOZ
@project: myDiscord
@file: create_account.py
@licence: GPLv3
"""

import os
import mariadb
from dotenv import load_dotenv
import customtkinter as ctk
import tkinter.messagebox as tkmb
from constants import *
from gui_message import *

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupère les informations de connexion à la base de données à partir des variables d'environnement
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Fonction pour revenir à la page de connexion
def back_to_login():
    # Ferme la fenêtre actuelle
    app.destroy()
    # Exécute login.py
    os.system("python login.py")

class CreateAccount:
    def __init__(self, master):
        self.master = master
        self.gui_create_account()

    def gui_create_account(self):
        frame = ctk.CTkFrame(master=self.master)
        frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        frame.pack(pady=120, padx=400, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Create Account', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Name", fg_color=FG_TEXT_FIELD,
                                        text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                        placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_entry.pack(pady=12, padx=10)

        self.user_password = ctk.CTkEntry(master=frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD,
                                           text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                           placeholder_text_color=TEXT_COLOR, show="*", font=FONT, width=250)
        self.user_password.pack(pady=12, padx=30)

        button_frame = ctk.CTkFrame(master=frame)
        button_frame.pack(pady=12, padx=10)

        create_account_label = ctk.CTkLabel(master=button_frame, text='Create Account', bg_color=FG_SECOND_COLOR,
                                            font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        create_account_label.grid(row=1, column=1)
        create_account_label.bind("<Button-1>", lambda event: self.create_account())

        # Création d'un label pour le texte "Back to login"
        back_to_login_label = ctk.CTkLabel(master=button_frame, text='Back to login', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        back_to_login_label.grid(row=1, column=2)
        back_to_login_label.bind("<Button-1>", lambda event: back_to_login())  # Ouvre la fonction back_to_login lorsqu'on clique dessus


    def create_account(self):
        name = self.user_entry.get()
        password = self.user_password.get()
        try:
            conn = mariadb.connect(
                user=db_user,
                password=db_password,
                host=db_host,
                port=3306,
                database=db_name
            )
            cursor = conn.cursor()
            cursor.execute("INSERT INTO user (name, password) VALUES (%s, %s)", (name, password))
            conn.commit()
            tkmb.showinfo(title="Account Created", message="Account created successfully")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        finally:
            if conn:
                conn.close()
        
        self.open_gui_message(name)

    def open_gui_message(self, current_user):
        self.master.destroy()
        os.system(f"python gui_message.py {current_user}")


# Crée une instance de CTk pour la fenêtre principale
app = ctk.CTk()
app.geometry("1200x700")
app.configure(fg_color=FG_COLOR)
app.title("Create Account")

# Crée une instance de la classe CreateAccount
create_account = CreateAccount(app)
# Lance la boucle principale de l'application
app.mainloop()
