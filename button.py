#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@author: Bruno Coulet

@file: button.py
@created: 08/02/2024

@project: myDiscord
@licence: GPLv3
"""


class Button:
    def __init__(self, screen, command, text, font = ("helvetica", 15), bg = 'black', highlightcolor = 'orange', fg = "white"):
        self.screen = screen
        self.text = text
        self.font = font
        self.bg = bg
        self.highlightcolor = highlightcolor
        self.fg = fg
        self.command = command
