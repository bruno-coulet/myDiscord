#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Lucas SAVIOZ
@project: myDiscord
@file: login.py
@licence: GPLv3
"""

import os
from constants import *
from dotenv import load_dotenv
import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import mysql.connector
from create_account import *
from gui_message import *

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les informations de connexion à la base de données à partir des variables d'environnement
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

######## Partie Fonctions ########

# Fonction principale pour lancer la connexion de l'utilisateur
def start_login_process():
    # Appel de la fonction user_login()
    user_login()

# Fonction de vérification de connexion
def user_login():
    name = user_entry.get()  # Récupérer le nom d'utilisateur depuis le champ de saisie
    password = user_password.get()  # Récupérer le mot de passe depuis le champ de saisie
    # Connexion à la base de données et vérification des informations d'identification de l'utilisateur
    try:
        connection = mysql.connector.connect(host=db_host,
                                             database=db_name,
                                             user=db_user,
                                             password=db_password)
        if connection.is_connected():
            cursor = connection.cursor()
            # Exécute une requête pour vérifier les informations d'identification de l'utilisateur
            cursor.execute("SELECT * FROM user WHERE name = %s AND password = %s", (name, password))
            row = cursor.fetchone()
            if row:
                tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
                open_message()  # Ouvre le fichier message.py après une connexion réussie
            else:
                tkmb.showerror(title="Login Failed", message="Invalid name and Password")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Fonction pour ouvrir le fichier channel.py
def open_message():
    os.system("python message.py")

######## Partie GUI ########

app = ctk.CTk()
app.geometry("1200x700")
app.configure(fg_color=FG_COLOR)
app.title("myDiscord")

label = ctk.CTkLabel(app, text="Welcome to Discord !", font= TITLE_FONT, text_color=TEXT_COLOR)
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)  # Définit la couleur de fond du cadre
frame.pack(pady=120, padx=400, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Please, Login !', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Name", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
user_entry.pack(pady=12, padx=10)

user_password = ctk.CTkEntry(master=frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, show="*", font=FONT, width=250)
user_password.pack(pady=12, padx=30)

# Création d'un sous-frame pour aligner les boutons à côté des entrées de texte
button_frame = ctk.CTkFrame(master=frame)
button_frame.pack(pady=12, padx=10)

# Création d'un label pour le texte "Login"
login_label = ctk.CTkLabel(master=button_frame, text='Login', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
login_label.grid(row=1, column=1)
login_label.bind("<Button-1>", lambda event: user_login())  # Exécute la fonction de connexion lorsqu'on clique dessus

# Création d'un label pour le texte "Create Account"
create_account_label = ctk.CTkLabel(master=button_frame, text='Create Account', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
create_account_label.grid(row=1, column=2)
create_account_label.bind("<Button-1>", lambda event: create_account())  # Ouvre la fenêtre de création de compte lorsqu'on clique dessus


checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me', font=FONT, text_color=TEXT_COLOR, border_color=BORDER_COLOR)
checkbox.pack(pady=12, padx=10)

# Appel de la fonction principale pour lancer le processus de connexion au démarrage
start_login_process()

app.mainloop()