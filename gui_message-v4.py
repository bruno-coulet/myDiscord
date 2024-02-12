#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: button.py
@created: 11/02/2024

@project: myDiscord
@licence: GPLv3
"""

import customtkinter


user_name = "user_name"
current_channel = "current_channel"

def view_channels():
    print("view channels")

def send_message():
    print("send message")

def log_out():
    print("log out")

def checkboxe_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())


    
class CheckboxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="message 1")
        self.checkbox_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="message 2")
        self.checkbox_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_3 = customtkinter.CTkCheckBox(self, text="message 3")
        self.checkbox_3.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")
        self.checkbox_4 = customtkinter.CTkCheckBox(self, text="message 4")
        self.checkbox_4.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")

    # NE MARCHE PAS, censé print le text de la checkboxe
    def get(self):
        checked_checkboxes = []
        if self.checkbox_1.get() == 1:
            checked_checkboxes.append(self.checkbox_1.cget("text"))
        if self.checkbox_2.get() == 1:
            checked_checkboxes.append(self.checkbox_2.cget("text"))
        if self.checkbox_3.get() == 1:
            checked_checkboxes.append(self.checkbox_3.cget("text"))
        return checked_checkboxes
    


class Message(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Messagerie")
        self.geometry("600x700")
        # gives an equal weight to column 0 and column 1 .
        self.grid_columnconfigure((0, 1), weight=1)


        # ----  WINDOW TITLE - ROW 0     -------
        title_label = customtkinter.CTkLabel(self, text=f"Bienvenue dans la messagerie {user_name}", font=("Helvetica", 20))
        title_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        

        # ----  CHANNEL FRAME - ROW 1     -------

        self.channel_frame = customtkinter.CTkFrame(self)
        self.channel_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.channel_frame.grid_columnconfigure((0, 1), weight=1)
        # bouton ROW 1/0
        self.button_create_channel = customtkinter.CTkButton(self.channel_frame, text="Autre channel", command=view_channels)
        self.button_create_channel.grid(row=0, column=1, padx=20, pady=20, sticky="w")
        # ----  CHANNEL FRAME - CURRENT CHANNEL under frame  - ROW 1/0    ---
        self.current_channel_frame = customtkinter.CTkFrame(self.channel_frame)
        self.current_channel_frame.grid(row=0, column=0, padx=10, pady=(10, 0))

        current_channel_label = customtkinter.CTkLabel(self.current_channel_frame, text=f"Channel actuel : {current_channel}", font=("Helvetica", 20))
        current_channel_title = customtkinter.CTkLabel(self.current_channel_frame, text="Les courges ont encore augmentées.", font=("Helvetica", 15))
        # title label  ROW 1/0/0
        current_channel_label.grid(row=0, column=0, padx=20, pady=20)
        # title value  ROW 1/0/1 
        current_channel_title.grid(row=1, column=0, padx=20, pady=20)


        # ---- CHANNEL FRAME - OLD MESSAGES UNDER FRAME  - ROW 1 /2    ---
        self.old_messages_frame = customtkinter.CTkFrame(self.channel_frame)
        self.old_messages_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew", columnspan=2)
        self.old_messages_frame.grid_columnconfigure((0, 1), weight=1)

        # existant messages - checkboxe for each
        self.checkbox_frame = CheckboxFrame(self.channel_frame)
        self.checkbox_frame.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="ew")
        # ... prévoir ascenceur




        # ----  NEW MESSAGE FRAME  - ROW 2    ---
        
        self.message_frame = customtkinter.CTkFrame(self)
        self.message_frame.grid(row=2, column=0, padx=10, pady=(10, 0))
        self.message_frame.grid_columnconfigure((0, 1), weight=1)
        # New message - label
        new_message_label = customtkinter.CTkLabel(self.message_frame, text="Nouveau Message.", font=("Helvetica", 20))
        new_message_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)
        # new message - is either text or audio message
        self.checkbox_1 = customtkinter.CTkCheckBox(self.message_frame, text="Message texte")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self.message_frame, text="Message audio")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(20, 20), sticky="w")
        # new message - text input area
        entry_text = customtkinter.CTkEntry(self.message_frame, width=400, height=100)
        entry_text.grid(row=2, column=0, padx=10, pady=10)
        # new message - send message button
        self.button_send_message = customtkinter.CTkButton(self.message_frame, text="Publier le message", command=lambda: print("send message", entry_text.get()))
        self.button_send_message.grid(row=3, column=0, padx=20, pady=20)




        # # ----OLD MESSAGE FRAME  - ROW 3    ---
        
        # self.old_message_frame = customtkinter.CTkFrame(self)
        # self.old_message_frame.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="nswe")
        # self.old_message_frame.grid_columnconfigure((0, 1), weight=1)
        # # existant messages - Label
        # old_messages_label = customtkinter.CTkLabel(self.old_message_frame, text="Messages du channel.")
        # old_messages_label.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        # # existant messages - checkboxe for each
        # self.checkbox_1 = customtkinter.CTkCheckBox(self.old_message_frame, text="message 1")
        # self.checkbox_1.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        # self.checkbox_2 = customtkinter.CTkCheckBox(self.old_message_frame, text="message 2")
        # self.checkbox_2.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
        # self.checkbox_3 = customtkinter.CTkCheckBox(self.old_message_frame, text="message 3")
        # self.checkbox_3.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="w")
        # self.checkbox_4 = customtkinter.CTkCheckBox(self.old_message_frame, text="message 4")
        # self.checkbox_4.grid(row=2, column=1, padx=10, pady=(10, 0), sticky="w")
        # # ... prévoir ascenceur


        #  log out - button
        self.button_log_out = customtkinter.CTkButton(self, text="Se déconnecter", command=log_out)
        self.button_log_out.grid(row=7 , column=0, padx=20, pady=20)

    def checkboxe_callback(self):
        print("checked checkboxes:", self.checkbox_frame.get())


message = Message()
message.mainloop()