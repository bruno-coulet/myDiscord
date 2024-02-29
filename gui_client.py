# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON

@file: gui_client.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
import customtkinter as ctk

from client import Client


class GuiClient(Client):
    """
    A class that allows you to interact with the Database server
    """
    def __init__(self):
        super().__init__()

    def gui_register(self):
        """
        Registers the user with the GUI
        :return: None
        """
        pass

    def gui_login(self):
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
        pass


if __name__ == "__main__":
    app = GuiClient()
    app.start()
