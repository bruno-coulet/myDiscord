#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Lucas SAVIOZ
@project: myDiscord
@file: create_account.py
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

# Fonction pour revenir à la page de connexion
def back_to_login():
    # Ferme la fenêtre actuelle
    app.destroy()
    # Exécute login.py
    os.system("python login.py")

# Fonction de création de compte dans la base de données
def create_user(name, firstname, email, password):
    try:
        connection = mysql.connector.connect(host=db_host,
                                             database=db_name,
                                             user=db_user,
                                             password=db_password)
        if connection.is_connected():
            cursor = connection.cursor()
            # Insère les données dans la base de données
            sql_query = """INSERT INTO user (name, first_name, email, password)
                            VALUES (%s, %s, %s, %s)"""
            user_data = (name, firstname, email, password)
            cursor.execute(sql_query, user_data)
            connection.commit()
            print("User created successfully")
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

# Fonction de création de compte
def create_account_logic(name, firstname, email, password):
    if not name or not firstname or not email or not password:
        tkmb.showwarning(title='Missing Fields', message='Please fill in all required fields.')
    else:
        create_user(name, firstname, email, password)
        tkmb.showinfo(title="Account Created", message="Account created successfully")

def create_account():
    name = name_entry.get()
    firstname = firstname_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    create_account_logic(name, firstname, email, password)


######## Partie GUI ########

app = ctk.CTk()
app.geometry("1200x700")
app.configure(fg_color=FG_COLOR)
app.title("Create Account")

label = ctk.CTkLabel(app, text="Not account yet ? Don't be cry", text_color=TEXT_COLOR, font=TITLE_FONT)
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)  # Couleur de fond du cadre
frame.pack(pady=120, padx=400, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Create your account now !', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
label.pack(pady=12, padx=10)

name_entry = ctk.CTkEntry(master=frame, placeholder_text="Name", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT)
name_entry.pack(pady=12, padx=10)

firstname_entry = ctk.CTkEntry(master=frame, placeholder_text="Firstname", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT)
firstname_entry.pack(pady=12, padx=10)

email_entry = ctk.CTkEntry(master=frame, placeholder_text="Email", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT)
email_entry.pack(pady=12, padx=10)

password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, show="*", font=FONT)
password_entry.pack(pady=12, padx=10)

# Création d'un sous-frame pour aligner les boutons à côté des entrées de texte
button_frame = ctk.CTkFrame(master=frame)
button_frame.pack(pady=12, padx=10)

# Création d'un label pour le texte "Create"
create_label = ctk.CTkLabel(master=button_frame, text='Create', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
create_label.grid(row=1, column=1)
create_label.bind("<Button-1>", lambda event: create_account())  # Ouvre la fonction create_account lorsqu'on clique dessus

# Création d'un label pour le texte "Back to login"
back_to_login_label = ctk.CTkLabel(master=button_frame, text='Back to login', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
back_to_login_label.grid(row=1, column=2)
back_to_login_label.bind("<Button-1>", lambda event: back_to_login())  # Ouvre la fonction back_to_login lorsqu'on clique dessus

app.mainloop()
