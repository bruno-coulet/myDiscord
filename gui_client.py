# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON

@file: gui_client.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
from client import Client

from constants import *


class GuiClient(Client, ctk.CTk):
    """
    A class that allows you to interact with the Database server
    """
    def __init__(self):
        Client.__init__(self)
        ctk.CTk.__init__(self)
        self.wm_title("Chat GUI Client")
        self.geometry("800x600")
        self.iconbitmap("images/blue-icon.ico")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)

    def gui_login(self):
        """
        The GUI login
        :return: None
        """

        pass

    def gui_register(self):
        """
        Registers the user with the GUI
        :return: None
        """
        pass

    def gui_message(self):
        """
        Connect the user with the GUI
        :return: None
        """
        pass

    def gui_logout(self):
        """
        Disconnect the user with the GUI
        :return: None
        """
        self.logout()

    def start(self):
        """
        Starts the GUI client
        :return: None
        """
        if self.get_state() is False:
            self.gui_login()
        else:
            self.gui_message()


if __name__ == "__main__":
    app = GuiClient()
    app.start()
