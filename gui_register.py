#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: gui_register.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
import re
import time
from client import Client
from db import Db
from constants import *


class GuiRegister(Client, ctk.CTk):
    """
    Class for GUI registering
    """
    def __init__(self):
        Client.__init__(self)
        ctk.CTk.__init__(self)
        self.email = ''
        self.password = ''
        self.firstName = ''
        self.lastName = ''
        self.nickname = ''
        self.validate = False
        self.wm_title("Register new user")
        self.geometry("800x600")
        self.iconbitmap("images/blue-icon.ico")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)

        self.frame = ctk.CTkFrame(master=self)
        self.frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        self.frame.pack(pady=12, padx=10, fill='both', expand=True)

        label = ctk.CTkLabel(master=self.frame, text='Create New Account', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        self.user_email = ctk.CTkEntry(master=self.frame, placeholder_text="Email", fg_color=FG_TEXT_FIELD,
                                       text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                       placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_email.pack(pady=12, padx=10)

        self.user_nickname = ctk.CTkEntry(master=self.frame, placeholder_text="Nickname", fg_color=FG_TEXT_FIELD,
                                          text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                          placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_nickname.pack(pady=12, padx=10)

        self.user_firstname = ctk.CTkEntry(master=self.frame, placeholder_text="First Name", fg_color=FG_TEXT_FIELD,
                                           text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                           placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_firstname.pack(pady=12, padx=10)

        self.user_lastname = ctk.CTkEntry(master=self.frame, placeholder_text="Last Name", fg_color=FG_TEXT_FIELD,
                                          text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                          placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_lastname.pack(pady=12, padx=10)

        self.user_password = ctk.CTkEntry(master=self.frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD,
                                          text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                          placeholder_text_color=TEXT_COLOR, show="*", font=FONT, width=250)
        self.user_password.pack(pady=12, padx=30)

        # Case à cocher pour afficher le mot de passe
        self.show_password_var = ctk.IntVar()
        self.show_password_check = ctk.CTkCheckBox(master=self.frame, text="Show Password", text_color=TEXT_COLOR,
                                                   variable=self.show_password_var)
        self.show_password_check.pack(pady=12, padx=10)
        self.show_password_var.trace_add("write", self.login_password_visibility)

        self.button_create_account = ctk.CTkButton(master=self.frame, text="Create account", text_color=TEXT_COLOR,
                                                   command=self.create_account)
        self.button_create_account.pack(pady=12, padx=10)

        self.create_account_label = ctk.CTkLabel(master=self.frame, text='',
                                                 bg_color=FG_SECOND_COLOR,
                                                 font=FONT, text_color=TEXT_COLOR, cursor="hand2")

    def validation(self):
        """
        Validate the registration data
        :return: None
        """
        if self.validate:
            time.sleep(2)
            self.destroy()

    def login_password_visibility(self, *args):
        """
        Checks if the user to want to see the password
        :return:
        """
        if self.show_password_var.get():
            self.user_password.configure(show="")
        else:
            self.user_password.configure(show="*")

    def create_account(self):
        """
        Creates a new account and saves it
        :return:
        """
        self.create_account_label.destroy()
        self.email = self. user_email.get()
        self.password = self.user_password.get()
        self.firstName = self.user_firstname.get()
        self.lastName = self.user_lastname.get()
        self.nickname = self.user_nickname.get()
        if self.email and self.password and self.firstName and self.lastName:
            if self.valid_email():
                req = f"SELECT email FROM users WHERE email = '{self.email}'"
                db = Db()
                db.connect()
                if db.query(req):

                    self.create_account_label = ctk.CTkLabel(master=self.frame, text='Email already registered',
                                                             bg_color=FG_SECOND_COLOR,
                                                             font=FONT, text_color=TEXT_COLOR, cursor="hand2")
                    self.create_account_label.pack(pady=30, padx=10)
                else:
                    self.register(self.firstName, self.lastName, self.email, self.password, self.nickname)
                    self.create_account_label = ctk.CTkLabel(master=self.frame, text='Registered',
                                                             bg_color=FG_SECOND_COLOR,
                                                             font=FONT, text_color=TEXT_COLOR, cursor="hand2")
                    self.create_account_label.pack(pady=30, padx=10)
                    self.validate = True
                    self.update()
                    self.validation()
                db.disconnect()

            else:
                self.create_account_label = ctk.CTkLabel(master=self.frame, text='Invalid Email',
                                                         bg_color=FG_SECOND_COLOR,
                                                         font=FONT, text_color=TEXT_COLOR, cursor="hand2")
                self.create_account_label.pack(pady=30, padx=10)
        else:
            self.create_account_label = ctk.CTkLabel(master=self.frame, text='All Fields Required',
                                                     bg_color=FG_SECOND_COLOR,
                                                     font=FONT, text_color=TEXT_COLOR, cursor="hand2")
            self.create_account_label.pack(pady=30, padx=10)

    def valid_email(self):
        """
        Checks if the email is valid
        :return: Bool
        """
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.fullmatch(regex, self.email):
            return True
        else:
            return False

    def start(self):
        """
        Starts the GUI registration
        :return: None
        """
        self.mainloop()


if __name__ == "__main__":
    app = GuiRegister()
    app.start()
