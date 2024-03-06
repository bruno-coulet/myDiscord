#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: gui_login.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
from client import Client
from gui_register import GuiRegister
from gui_messages import GuiMessages
from constants import *


class GuiLogin(Client, ctk.CTk):
    """
    GUI login class
    """
    def __init__(self):
        Client.__init__(self)
        ctk.CTk.__init__(self)
        self.wm_title("Login to Chat Client")
        self.geometry("800x600")
        self.iconbitmap("images/blue-icon.ico")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)
        self.email = ''
        self.password = ''

        self.frame = ctk.CTkFrame(master=self)
        self.frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        self.frame.pack(pady=12, padx=10, fill='both', expand=True)

        label = ctk.CTkLabel(master=self.frame, text='Please, Login !', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        self.user_email = ctk.CTkEntry(master=self.frame, placeholder_text="Email", fg_color=FG_TEXT_FIELD,
                                       text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                       placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_email.pack(pady=12, padx=10)

        self.user_password = ctk.CTkEntry(master=self.frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD,
                                          text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                          placeholder_text_color=TEXT_COLOR, show="*", font=FONT, width=250)
        self.user_password.pack(pady=12, padx=30)

        self.show_password_var = ctk.IntVar()
        self.show_password_check = ctk.CTkCheckBox(master=self.frame, text="Show Password", text_color=TEXT_COLOR,
                                                   variable=self.show_password_var)
        self.show_password_check.pack(pady=12, padx=10)
        self.show_password_var.trace_add("write", self.login_password_visibility)

        self.button_connection = ctk.CTkButton(master=self.frame, text="Connection", command=self.login_user)
        self.button_connection.pack(pady=12, padx=10)

        self.button_connection = ctk.CTkButton(master=self.frame, text="Register", command=self.register_user)
        self.button_connection.pack(pady=12, padx=10)

        self.login_label = ctk.CTkLabel(master=self.frame, text='', bg_color=FG_SECOND_COLOR, font=FONT,
                                        text_color=TEXT_COLOR, cursor="hand2", padx=10)
        self.login_label.pack(pady=12, padx=12)

    def login_password_visibility(self, *args):
        """
        Checks if the user want to see the password
        :return:
        """
        if self.show_password_var.get() == 1:
            self.user_password.configure(show="")
        else:
            self.user_password.configure(show="*")

    def register_user(self):
        """
        Register user action
        :return:
        """
        # self.destroy()
        register = GuiRegister()
        register.mainloop()
        self.update()

    def login_user(self):
        """
        Login user action
        :return: None
        """
        self.login_label.destroy()
        self.update()
        self.email, self.password = self.user_email.get(), self.user_password.get()
        self.connect(email=self.email, password=self.password)
        if self.get_state():
            message = GuiMessages()
            message.set_id_connect(self.get_id())
            message.set_uuid(self.get_uuid())
            message.change_state_connect()
            self.destroy()
            message.mainloop()
        else:
            self.login_label = ctk.CTkLabel(master=self.frame, text='Bad credentials', bg_color=FG_SECOND_COLOR, font=FONT,
                                            text_color=TEXT_COLOR, cursor="hand2", padx=10)
            self.login_label.pack(pady=12, padx=12)

    def start(self):
        """
        Start the GUI
        :return: None
        """
        self.mainloop()


if __name__ == '__main__':
    app = GuiLogin()
    app.start()
