# -*- coding: utf-8 -*-
"""
@authors: Cyril GENISSON

@file: gui_messages.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""
from client import Client
from constants import *


class GuiMessages(Client, ctk.CTk):
    def __init__(self):
        Client.__init__(self)
        ctk.CTk.__init__(self)
        self.wm_title("Chat Client")
        self.geometry("800x600")
        self.iconbitmap("images/blue-icon.ico")
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("dark-blue")
        self.configure(fg_color=FG_COLOR)
        self.resizable(False, False)
        #self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        #self.columnconfigure(2, weight=1)

        self.rooms_frame = ctk.CTkFrame(master=self, width=200, height=600)
        self.rooms_frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        self.rooms_frame.grid(row=0, column=0, sticky="nsew")

        self.label = ctk.CTkLabel(master=self.rooms_frame, text="Rooms")
        self.label.pack(padx=100, pady=10)


        self.messages_frame = ctk.CTkFrame(master=self)
        self.messages_frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        self.messages_frame.grid(row=0, column=1, sticky="nsew")

        self.barrel_frame = ctk.CTkFrame(master=self)
        self.barrel_frame.grid(row=2, column=1, sticky="nsew")


if __name__ == "__main__":
    app = GuiMessages()
    app.mainloop()
