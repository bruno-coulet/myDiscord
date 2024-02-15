#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Lucas SAVIOZ
@project: myDiscord
@file: create_account.py
@licence: GPLv3
"""

import customtkinter as ctk 
import tkinter.messagebox as tkmb 
import os

# Fonction pour revenir à la page de connexion
def back_to_login():
    # Fermer la fenêtre actuelle
    app.destroy()
    # Exécuter login.py
    os.system("python login.py")

# Fonction de création de compte
def create_account_logic(username, password):
    if not username or not password:
        tkmb.showwarning(title='Missing Fields', message='Please fill in all required fields.')
    else:
        tkmb.showinfo(title="Account Created", message="Account created successfully")

def create_account():
    username = user_entry.get()
    password = user_pass.get()
    create_account_logic(username, password)

# Votre code GUI existant
app = ctk.CTk()
app.geometry("1200x700")
app.title("Create Account")

label = ctk.CTkLabel(app, text="Create Account")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

user_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
user_entry.pack(pady=12, padx=10)

user_pass = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
user_pass.pack(pady=12, padx=10)

button_create = ctk.CTkButton(master=frame, text='Create Account', command=create_account)
button_create.pack(pady=12, padx=10)

# Bouton pour revenir à la page de connexion
button_back_to_login = ctk.CTkButton(master=frame, text='Back to Login', command=back_to_login)
button_back_to_login.pack(pady=12, padx=10)

app.mainloop()
