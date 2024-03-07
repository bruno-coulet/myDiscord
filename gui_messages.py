#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Cyril Génisson

@file: gui_messages.py
@created: 07/03/2024

@project: myDiscord
@licence: GPLv3
"""
import tkinter.messagebox as tkmb
from client import Client
from audio import *
from constants import *


class GuiMessages(Client, ctk.CTk):
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
        self.current_user = None
        self.gui_message()

    def gui_message(self):
        """
        Creates the GUI message box
        :return:
        """
        frame = ctk.CTkFrame(master=self)
        frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR, bg_color=FG_COLOR)
        frame.pack(pady=50, padx=200, fill='both', expand=True)

        self.label_text = f'Room: {self.channel_name}'
        label = ctk.CTkLabel(master=frame, text=self.label_text, text_color=TEXT_COLOR, bg_color=FG_SECOND_COLOR,
                             font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        message_frame = ctk.CTkScrollableFrame(master=frame, border_width=1, border_color=BORDER_COLOR)
        message_frame.pack(pady=12, padx=10, fill='both', expand=True)

        self.message_display = ctk.CTkLabel(master=message_frame, text="", bg_color=FG_SECOND_COLOR, fg_color=FG_COLOR,
                                            text_color=TEXT_COLOR, font=FONT, width=80, height=30, anchor='nw',
                                            justify='left', wraplength=800)
        self.message_display.pack(pady=10, padx=10)
        self.message_display.configure(bg_color=FG_COLOR, fg_color=FG_COLOR)

        entry_frame = ctk.CTkFrame(master=frame)
        entry_frame.pack(pady=12, padx=10, fill='x')

        self.user_entry = ctk.CTkEntry(master=entry_frame, placeholder_text="Type your message here",
                                  fg_color=FG_SECOND_COLOR, text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                  placeholder_text_color=TEXT_COLOR, bg_color=FG_SECOND_COLOR, font=FONT, width=60)
        self.user_entry.pack(side='left', padx=5, fill='x', expand=True)

        send_button = ctk.CTkButton(master=frame, text="SEND", font=FONT, bg_color=FG_SECOND_COLOR,
                                    fg_color=FG_SECOND_COLOR, command=self.send_message)
        send_button.pack(pady=5, padx=10)

        audio_button = ctk.CTkButton(master=frame, text="Audio Message", font=FONT, bg_color=FG_SECOND_COLOR,
                                     fg_color=FG_SECOND_COLOR, command=self.send_audio_message)
        audio_button.pack(pady=5, padx=10)

    def send_message(self):
        """
        Function to send messages
        :return:
        """
        message = self.user_entry.get()
        if message:
            current_text = self.message_display.cget("text")
            updated_text = f"{current_text}\n{self.current_user}: {message}"
            self.message_display.configure(text=updated_text)
            self.user_entry.delete(0, 'end')

    def send_audio_message(self):
        """
        Send audio
        :return: Not implemented
        """
        records = record(5)
        play(records)
        tkmb.showinfo("Audio Message", "Audio message functionality not implemented yet.")

    def start(self):
        """
        Starts the GUI loop
        :return:
        """
        self.mainloop()


if __name__ == "__main__":
    gui_message = GuiMessages()
    gui_message.mainloop()
