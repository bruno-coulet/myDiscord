import customtkinter as ctk
import tkinter as tk
from constants import *

class Login(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("600x700")

        # Création du cadre de connexion avec la couleur de fond spécifiée et la taille définie
        window_width = 600  # largeur de la fenêtre principale
        window_height = 700  # hauteur de la fenêtre principale
        self.login_frame = ctk.CTkFrame(self, bg_color=BG_COLOR, width=window_width, height=window_height)
        self.login_frame.pack(fill="both", expand=True)

        
        ####### Paramètres des éléments visuels de la fenêtre Login #######

        self.title_label = ctk.CTkLabel(self.login_frame, text="Login", font=TITLE_FONT)
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.login_frame.grid_columnconfigure(0, weight=1)  # Permet d'étirer la première colonne pour centrer le label
        self.login_frame.grid_columnconfigure(1, weight=1)  # Permet d'étirer la deuxième colonne pour centrer le label


        self.username_label = ctk.CTkLabel(self.login_frame, text="Name:", font=SUBTITLE_FONT)
        self.username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = self.create_entry(self.login_frame, "Name", font=SUBTITLE_FONT)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.firstname_label = ctk.CTkLabel(self.login_frame, text="Firstname:", font=SUBTITLE_FONT)
        self.firstname_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.firstname_entry = self.create_entry(self.login_frame, "Firstname", font=SUBTITLE_FONT)
        self.firstname_entry.grid(row=2, column=1, padx=10, pady=5)

        self.password_label = ctk.CTkLabel(self.login_frame, text="Password:", font=SUBTITLE_FONT)
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = self.create_entry(self.login_frame, "Password", font=SUBTITLE_FONT, show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Bouton créer un compte
        self.create_account_button = ctk.CTkButton(self.login_frame, text="Create account", font=SUBTITLE_FONT, bg_color=HIGHLIGHT_COLOR, command=self.create_account)
        self.create_account_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Bouton se connecter
        self.login_button = ctk.CTkButton(self.login_frame, text="Login", font=SUBTITLE_FONT, bg_color=HIGHLIGHT_COLOR, command=self.login)
        self.login_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        # Centrage des colonnes
        self.login_frame.grid_columnconfigure(0, weight=1)
        self.login_frame.grid_columnconfigure(1, weight=1)

        # Réactivité de l'interface
        self.make_responsive()

    def make_responsive(self):
        # Pour rendre la fenêtre responsive, les lignes doivent s'adapter au redimensionnement de la fenêtre
        for row in range(6):
            self.login_frame.grid_rowconfigure(row, weight=1)

    def create_entry(self, parent, default_text, **kwargs):
        # Zones de textes
        entry = ctk.CTkEntry(parent, width=100, **kwargs)
        entry.default_text = default_text
        entry.insert(0, entry.default_text)
        entry.bind("<FocusIn>", lambda event, entry=entry: self.entry_click_delete(event, entry))
        entry.bind("<FocusOut>", lambda event, entry=entry: self.entry_leave(event, entry))
        return entry

    def entry_click_delete(self, event, entry):
        if entry.get() == entry.default_text:
            entry.delete(0, tk.END)
            entry.configure(fg='black')

    def entry_leave(self, event, entry):
        if not entry.get():
            entry.insert(0, entry.default_text)
            entry.configure(fg='grey')

    def create_account(self):
        print("Create account in process")

    def login(self):
        print("Login in process")

if __name__ == "__main__":
    app = Login()
    app.mainloop()
