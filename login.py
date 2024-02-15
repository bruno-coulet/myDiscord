#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Lucas SAVIOZ
@project: myDiscord
@file: login.py
@licence: GPLv3
"""

import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import os


######## Partie Fonctions ########

# Fonction pour changer de page vers create_account.py
def open_create_account():
    # Fermer la fenêtre actuelle
    app.destroy()
    # Exécute le fichier create_account.py
    os.system("python create_account.py")

# Fonction de vérification de connexion
def user_login(username, password):

    valid_username = "admin"
    valid_password = "root"

    if username == valid_username and password == valid_password:
        tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
    elif username == valid_username:
        tkmb.showwarning(title='Wrong Password', message='Please check your password')
    else:
        tkmb.showerror(title="Login Failed", message="Invalid Username and Password")

# Fonction de connexion
def login():
    username = user_entry.get()
    password = user_password.get()
    user_login(username, password)


######## Partie GUI ########
    
app = ctk.CTk()
app.geometry("1200x700")
app.title("myDiscord")

label = ctk.CTkLabel(app, text="Welcome !")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

label = ctk.CTkLabel(master=frame, text='Login')
label.pack(pady=12, padx=10)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_password = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_password.pack(pady=12, padx=10)

button_login = ctk.CTkButton(master=frame, text='Login', command=login)
button_login.pack(pady=12, padx=10)

# Bouton "Account" pour ouvrir create_account.py
button_create_account = ctk.CTkButton(master=frame, text='Create Account', command=open_create_account)
button_create_account.pack(pady=12, padx=10)

checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
checkbox.pack(pady=12, padx=10)

app.mainloop()