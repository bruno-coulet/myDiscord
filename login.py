#!/usr/bin/venv python3
# -*- coding: utf-8 -*-
"""
@authors: Lucas SAVIOZ
@project: myDiscord
@file: login.py
@licence: GPLv3
"""

import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from constants import *


# GUI theme - dark
ctk.set_appearance_mode(BG_COLOR) 

# color theme - dark-blue 
ctk.set_default_color_theme(HIGHLIGHT_COLOR) 

app = ctk.CTk() 
app.geometry("1200x700") 
app.title("myDiscord") 


def login(): 

	username = "admin"
	password = "root"
	new_window = ctk.CTkToplevel(app) 

	new_window.title("Messagerie") 

	new_window.geometry("1200x700") 

	if user_entry.get() == username and user_pass.get() == password: 
		tkmb.showinfo(title="Login Successful",message="You have logged in Successfully") 
		ctk.CTkLabel(new_window,text="You are actually connect").pack() 
	elif user_entry.get() == username and user_pass.get() != password: 
		tkmb.showwarning(title='Wrong password',message='Please check your password') 
	elif user_entry.get() != username and user_pass.get() == password: 
		tkmb.showwarning(title='Wrong username',message='Please check your username') 
	else: 
		tkmb.showerror(title="Login Failed",message="Invalid Username and password") 


label = ctk.CTkLabel(app,text="Welcome !") 
label.pack(pady=20) 

frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 

label = ctk.CTkLabel(master=frame,text='Login') 
label.pack(pady=12,padx=10) 


user_entry= ctk.CTkEntry(master=frame,placeholder_text="Username") 
user_entry.pack(pady=12,padx=10) 

user_pass= ctk.CTkEntry(master=frame,placeholder_text="Password",show="*") 
user_pass.pack(pady=12,padx=10) 


button = ctk.CTkButton(master=frame,text='Login',command=login) 
button.pack(pady=12,padx=10) 

checkbox = ctk.CTkCheckBox(master=frame,text='Remember Me') 
checkbox.pack(pady=12,padx=10) 


app.mainloop()