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
from gui_message import GuiMessage

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupére les informations de connexion à la base de données à partir des variables d'environnement
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

class CreateAccount:
    def __init__(self, master):
        self.master = master
        self.gui_create_account()

    def gui_create_account(self):
        self.master.geometry("1200x700")
        self.master.configure(fg_color=FG_COLOR)
        self.master.title("Create Account")

        label = ctk.CTkLabel(self.master, text="Not account yet ? Don't be cry", text_color=TEXT_COLOR, font=TITLE_FONT)
        label.pack(pady=20)

        frame = ctk.CTkFrame(master=self.master)
        frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)  # Couleur de fond du cadre
        frame.pack(pady=120, padx=400, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Create your account now !', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        self.name_entry = ctk.CTkEntry(master=frame, placeholder_text="Name", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT)
        self.name_entry.pack(pady=12, padx=10)

        self.firstname_entry = ctk.CTkEntry(master=frame, placeholder_text="Firstname", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT)
        self.firstname_entry.pack(pady=12, padx=10)

        self.email_entry = ctk.CTkEntry(master=frame, placeholder_text="Email", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, font=FONT)
        self.email_entry.pack(pady=12, padx=10)

        self.password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD, text_color=TEXT_COLOR, border_color=BORDER_COLOR, placeholder_text_color=TEXT_COLOR, show="*", font=FONT)
        self.password_entry.pack(pady=12, padx=10)

        # Création d'un sous-frame pour aligner les boutons à côté des entrées de texte
        button_frame = ctk.CTkFrame(master=frame)
        button_frame.pack(pady=12, padx=10)

        # Création d'un label pour le texte "Create"
        create_label = ctk.CTkLabel(master=button_frame, text='Create', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        create_label.grid(row=1, column=1)
        create_label.bind("<Button-1>", lambda event: self.create_account())  # Ouvre la fonction create_account lorsqu'on clique dessus

        # Création d'un label pour le texte "Back to login"
        back_to_login_label = ctk.CTkLabel(master=button_frame, text='Back to login', bg_color=FG_SECOND_COLOR, font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        back_to_login_label.grid(row=1, column=2)
        back_to_login_label.bind("<Button-1>", lambda event: self.back_to_login())  # Ouvre la fonction back_to_login lorsqu'on clique dessus

    def back_to_login(self):
        self.master.destroy()
        os.system("python login.py")

    def create_user(self, name, firstname, email, password):
        try:
            conn = mariadb.connect(
                user=db_user,
                password=db_password,
                host=db_host,
                port=3306,
                database=db_name
            )
            cursor = conn.cursor()
            sql_query = """INSERT INTO user (name, first_name, email, password)
                            VALUES (%s, %s, %s, %s)"""
            user_data = (name, firstname, email, password)
            cursor.execute(sql_query, user_data)
            conn.commit()
            print("User created successfully")
            return True
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def create_account(self):
        name = self.name_entry.get()
        firstname = self.firstname_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        # Appel de la logique de création de compte
        account_created_successfully = self.create_user(name, firstname, email, password)

        # Si le compte a été créé avec succès, redirigez l'utilisateur vers message.py
        if account_created_successfully:
            self.open_message()

    def open_message(self):
        # Ferme la fenêtre actuelle
        self.master.destroy()
        # Instancie la classe GuiMessage et exécute son instance
        app = ctk.CTk()
        gui_message = GuiMessage(app)
        app.mainloop()

if __name__ == "__main__":
    app = ctk.CTk()
    create_account_window = CreateAccount(app)
    app.mainloop()