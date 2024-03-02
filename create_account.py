#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Lucas SAVIOZ
@project: myDiscord
@file: create_account.py
@licence: GPLv3
"""

import os
from db import Db
from lib import hash_pass, check_pass
import tkinter.messagebox as tkmb
import customtkinter as ctk
from constants import *
from client import Client  

class CreateAccount:
    def __init__(self, master):
        self.master = master
        self.user_manager = Client()  # Initialisation de Client
        self.gui_create_account()

    def gui_create_account(self):
        frame = ctk.CTkFrame(master=self.master)
        frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        frame.pack(pady=120, padx=400, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Create Account', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        self.user_entry_nickname = ctk.CTkEntry(master=frame, placeholder_text="Nickname", fg_color=FG_TEXT_FIELD,
                                                 text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                                 placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_entry_nickname.pack(pady=12, padx=10)

        self.user_entry_firstname = ctk.CTkEntry(master=frame, placeholder_text="First Name", fg_color=FG_TEXT_FIELD,
                                                  text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                                  placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_entry_firstname.pack(pady=12, padx=10)

        self.user_entry_lastname = ctk.CTkEntry(master=frame, placeholder_text="Last Name", fg_color=FG_TEXT_FIELD,
                                                 text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                                 placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_entry_lastname.pack(pady=12, padx=10)

        self.user_entry_email = ctk.CTkEntry(master=frame, placeholder_text="Email", fg_color=FG_TEXT_FIELD,
                                              text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                              placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_entry_email.pack(pady=12, padx=10)

        self.user_entry_password = ctk.CTkEntry(master=frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD,
                                                 text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                                 placeholder_text_color=TEXT_COLOR, show="*", font=FONT, width=250)
        self.user_entry_password.pack(pady=12, padx=30)

        # Case à cocher pour afficher le mot de passe
        self.show_password_var = ctk.IntVar()
        self.show_password_check = ctk.CTkCheckBox(master=frame, text="Show Password", text_color=TEXT_COLOR, variable=self.show_password_var)
        self.show_password_check.pack(pady=12, padx=10)
        self.show_password_var.trace_add("write", self.toggle_password_visibility)

        button_frame = ctk.CTkFrame(master=frame)
        button_frame.pack(pady=12, padx=10)

        create_account_label = ctk.CTkLabel(master=button_frame, text='Create Account', bg_color=FG_SECOND_COLOR,
                                            font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        create_account_label.grid(row=1, column=1)
        create_account_label.bind("<Button-1>", lambda event: self.create_account())

        # Ajout du bouton "Back to Login"
        back_to_login_label = ctk.CTkLabel(master=button_frame, text='Back to login', bg_color=FG_SECOND_COLOR,
                                           font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        back_to_login_label.grid(row=1, column=2)
        back_to_login_label.bind("<Button-1>", lambda event: self.back_to_login())

    def toggle_password_visibility(self, *args):
        if self.show_password_var.get() == 1:
            self.user_entry_password.configure(show="")
        else:
            self.user_entry_password.configure(show="*")

    def create_account(self):
        nickname = self.user_entry_nickname.get()
        firstname = self.user_entry_firstname.get()
        lastname = self.user_entry_lastname.get()
        email = self.user_entry_email.get()
        password = self.user_entry_password.get()
        
        # Appel de la méthode register de Client pour enregistrer un nouvel utilisateur
        self.user_manager.register(firstname, lastname, email, password, nickname)
        tkmb.showinfo(title="Account Created", message="Account created successfully")

        # Ouvre gui_message.py
        self.open_gui_message(nickname)

    def open_gui_message(self, current_user):
        self.master.destroy()
        os.system(f"python gui_message.py {current_user}")

    # Méthode pour revenir à la page de connexion
    def back_to_login(self):
        # Ferme la fenêtre actuelle
        self.master.destroy()
        # Exécute login.py
        os.system("python login.py")

if __name__ == "__main__":
    app = ctk.CTk()
    app.geometry("1200x700")
    app.configure(fg_color=FG_COLOR)
    app.title("Create Account")

    create_account = CreateAccount(app)
    app.mainloop()
