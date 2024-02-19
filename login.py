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

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les informations de connexion à la base de données à partir des variables d'environnement
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Fonction pour changer de page vers create_account.py
def open_create_account():
    # Fermer la fenêtre actuelle
    app.destroy()
    # Exécute le fichier create_account.py
    os.system("python create_account.py")

# Fonction pour ouvrir le fichier channel.py
def open_channels():
    # Exécute le fichier channel.py
    os.system("python channel.py")

# Fonction de vérification de connexion
def user_login(username, password):
    # Connexion à la base de données et vérification des informations d'identification de l'utilisateur
    try:
        connection = mysql.connector.connect(host=db_host,
                                             database=db_name,
                                             user=db_user,
                                             password=db_password)
        if connection.is_connected():
            cursor = connection.cursor()
            # Exécute une requête pour vérifier les informations d'identification de l'utilisateur
            cursor.execute("SELECT * FROM user WHERE username = %s AND password = %s", (username, password))
            row = cursor.fetchone()
            if row:
                tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
                open_channels()  # Ouvre le fichier channels.py après une connexion réussie
            else:
                tkmb.showerror(title="Login Failed", message="Invalid Username and Password")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Fonction de connexion
def login():
    username = user_entry.get()
    password = user_password.get()
    user_login(username, password)


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
login_label.bind("<Button-1>", lambda event: login())  # Ouvre la fenêtre de connexion lorsqu'on clique dessus

# Création d'un label pour le texte "Create Account"
create_account_label = ctk.CTkLabel(master=button_frame, text='Create Account', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
create_account_label.grid(row=1, column=2)
create_account_label.bind("<Button-1>", lambda event: open_create_account())  # Ouvre la fenêtre de création de compte lorsqu'on clique dessus


checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me', font=FONT, text_color=TEXT_COLOR, border_color=BORDER_COLOR)
checkbox.pack(pady=12, padx=10)

app.mainloop()
