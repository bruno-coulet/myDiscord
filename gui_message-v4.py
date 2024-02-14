#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: gui_message.py
@created: 11/02/2024

@project: myDiscord
@licence: GPLv3
"""

import customtkinter as ctk
from constants import *

user_name = "user_name"
current_channel = "current_channel"

def view_channels():
    print("view channels")

def send_message():
    print("send message")

def log_out():
    print("log out")

def checkbox_callback(self):
        print("checked checkboxes:")


    
class ScrollableFrame(ctk.CTkScrollableFrame):

    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        """To make the MyCheckboxFrame class more dynamically usable, we pass a list of string values to the MyCheckboxFrame, which will be the text values of the checkboxes in the frame. Now the number of checkboxes is also arbitrary."""
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0))
            self.checkboxes.append(checkbox)


    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes


    

class Message(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Messagerie")
        self.geometry("600x700")
        self.grid_columnconfigure((0, 1), weight=1)
        # self.configure(fg_color="darkolivegreen3")


        # ----  WINDOW TITLE - ROW 0     -------
        title_label = ctk.CTkLabel(self, text=f"Bienvenue dans la messagerie {user_name}", font=(TITLE_FONT))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        title_label.configure(fg_color="darkolivegreen4")
        

        # ----  CHANNEL FRAME - ROW 1     -------

        self.channel_frame = ctk.CTkFrame(self)
        self.channel_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        self.channel_frame.grid_columnconfigure((0, 1), weight=1)
        # bouton ROW 1/0
        self.button_create_channel = ctk.CTkButton(self.channel_frame, text="Autre channel", command=view_channels)
        self.button_create_channel.grid(row=0, column=1, padx=20, pady=20, sticky="w")
        # ----  CHANNEL FRAME - CURRENT CHANNEL under frame  - ROW 1/0    ---
        self.current_channel_frame = ctk.CTkFrame(self.channel_frame)
        self.current_channel_frame.grid(row=0, column=0, padx=10, pady=(10, 0))

        current_channel_label = ctk.CTkLabel(self.current_channel_frame, text=f"Channel actuel : {current_channel}", font=SUBTITLE_FONT)
        current_channel_title = ctk.CTkLabel(self.current_channel_frame, text="Les courges ont encore augmentées.", font=FONT)
        # title label  ROW 1/0/0
        current_channel_label.grid(row=0, column=0, padx=20, pady=20)
        # title value  ROW 1/0/1 
        current_channel_title.grid(row=1, column=0, padx=20, pady=20)


        # ---- CHANNEL FRAME - OLD MESSAGES UNDER FRAME  - ROW 1 /2    ---
        # self.old_messages_frame = ctk.CTkFrame(self.channel_frame)
        # self.old_messages_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        # self.old_messages_frame.grid_columnconfigure((0, 1), weight=1)
        # self.old_messages_frame.configure(fg_color="darkolivegreen3")

        # existant messages
        self.frame_old_message = ScrollableFrame(self.channel_frame, "Messages existants", values=["Message 1", "Message 2", "Message 3", "Message 4", "Message 5", "Message 6","Message 1", "Message 2", "Message 3", "Message 4", "Message 5", "Message 6"])
        self.frame_old_message.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        self.frame_old_message.configure(fg_color="darkolivegreen4")
      

        # ----  NEW MESSAGE FRAME  - ROW 2    ---
        
        self.message_frame = ctk.CTkFrame(self)
        self.message_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        self.message_frame.grid_columnconfigure((0, 1), weight=1)
        self.message_frame.configure(fg_color="chartreuse4")
        # New message - label
        new_message_label = ctk.CTkLabel(self.message_frame, text="Nouveau Message.", font=SUBTITLE_FONT)
        new_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        # new message - is either text or audio message
        self.checkbox_text_message = ctk.CTkCheckBox(self.message_frame, text="Message texte")
        self.checkbox_text_message.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="w")
        self.checkbox_audio_message = ctk.CTkCheckBox(self.message_frame, text="Message audio")
        self.checkbox_audio_message.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="w")
        # new message - text input area
        entry_text = ctk.CTkEntry(self.message_frame, width=400, height=100)
        entry_text.grid(row=2, column=0, padx=10, pady=10)
        # new message - send message button
        self.button_send_message = ctk.CTkButton(self.message_frame, text="Publier le message", command=lambda: print("send message", entry_text.get()))
        self.button_send_message.grid(row=3, column=0, padx=20, pady=20)



        # ----  log out - button  - ROW 3    ---
        self.button_log_out = ctk.CTkButton(self, text="Se déconnecter", command=log_out)
        self.button_log_out.grid(row=3 , column=0, padx=20, pady=20)

    def  checkbox_callback(self):
        print("checkboxes sélectionnées:", self.checkbox_frame_old_message.get())



message = Message()
message.mainloop()