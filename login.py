import os
import mariadb
from dotenv import load_dotenv
import customtkinter as ctk
import tkinter.messagebox as tkmb
from constants import *

# Charge les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupère les informations de connexion à la base de données à partir des variables d'environnement
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

class Login:
    def __init__(self, master):
        self.master = master
        self.gui_login()

    def gui_login(self):
        frame = ctk.CTkFrame(master=self.master)
        frame.configure(fg_color=FG_SECOND_COLOR, border_width=2, border_color=BORDER_COLOR)
        frame.pack(pady=120, padx=400, fill='both', expand=True)

        label = ctk.CTkLabel(master=frame, text='Please, Login !', text_color=TEXT_COLOR, font=SUBTITLE_FONT)
        label.pack(pady=12, padx=10)

        self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Name", fg_color=FG_TEXT_FIELD,
                                        text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                        placeholder_text_color=TEXT_COLOR, font=FONT, width=250)
        self.user_entry.pack(pady=12, padx=10)

        self.user_password = ctk.CTkEntry(master=frame, placeholder_text="Password", fg_color=FG_TEXT_FIELD,
                                           text_color=TEXT_COLOR, border_color=BORDER_COLOR,
                                           placeholder_text_color=TEXT_COLOR, show="*", font=FONT, width=250)
        self.user_password.pack(pady=12, padx=30)

        # Création d'un sous-frame pour aligner les boutons à côté des entrées de texte
        button_frame = ctk.CTkFrame(master=frame)
        button_frame.pack(pady=12, padx=10)

        # Création d'un label pour le texte "Login"
        login_label = ctk.CTkLabel(master=button_frame, text='Login', bg_color=FG_SECOND_COLOR, font=FONT,
                                   text_color=TEXT_COLOR, cursor="hand2", padx=10)
        login_label.grid(row=1, column=1)
        login_label.bind("<Button-1>", lambda event: self.user_login())  # Exécute la fonction de user_login

        # Création d'un label pour le texte "Create Account"
        create_account_label = ctk.CTkLabel(master=button_frame, text='Create Account', bg_color=FG_SECOND_COLOR,
                                            font=FONT, text_color=TEXT_COLOR, cursor="hand2", padx=10)
        create_account_label.grid(row=1, column=2)
        create_account_label.bind("<Button-1>", lambda event: self.open_create_account())  # Ouvre la fenêtre de création de compte

        self.checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me', font=FONT, text_color=TEXT_COLOR,
                                        border_color=BORDER_COLOR)
        self.checkbox.pack(pady=12, padx=10)

    def user_login(self):
        name = self.user_entry.get()
        password = self.user_password.get()
        try:
            conn = mariadb.connect(
                user=db_user,
                password=db_password,
                host=db_host,
                port=3306,
                database=db_name
            )
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM user WHERE name = %s AND password = %s", (name, password))
            row = cursor.fetchone()
            if row:
                tkmb.showinfo(title="Login Successful", message="You have logged in successfully")
                # Si le login est réussi, ouvrez GuiMessage
                self.open_gui_message()
            else:
                tkmb.showerror(title="Login Failed", message="Invalid name and Password")
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        finally:
            if conn:
                conn.close()

    def open_create_account(self):
        self.master.destroy()
        os.system("python create_account.py")

    def open_gui_message(self):
        # Ferme la fenêtre de login
        self.master.destroy()
        # Ouvre l'interface GuiMessage
        os.system("python gui_message.py")


# Crée une instance de CTk pour la fenêtre principale
app = ctk.CTk()
app.geometry("1200x700")
app.configure(fg_color=FG_COLOR)
app.title("myDiscord")

# Crée une instance de la classe Login
login = Login(app)
# Lance la boucle principale de l'application
app.mainloop()
