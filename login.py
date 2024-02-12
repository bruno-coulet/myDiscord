import tkinter as tk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")

        # Création du cadre de connexion 
        self.login_frame = tk.Frame(self, padx=600, pady=700)
        # Taille de la fenêtre principale
        self.geometry("600x700")
        # Centrage de la fenêtre principale
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ####### Paramètres des éléments visuel de la fenêtre Login #######

        self.title_label = tk.Label(self.login_frame, text="Login", font=("Arial", 40))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.username_label = tk.Label(self.login_frame, text="Name:", font=("Arial", 12))
        self.username_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = self.create_entry(self.login_frame, "Name", font=("Arial", 12))
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        self.firstname_label = tk.Label(self.login_frame, text="Firstname:", font=("Arial", 12))
        self.firstname_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.firstname_entry = self.create_entry(self.login_frame, "Firstname", font=("Arial", 12))
        self.firstname_entry.grid(row=2, column=1, padx=10, pady=5)

        self.password_label = tk.Label(self.login_frame, text="Password:", font=("Arial", 12))
        self.password_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = self.create_entry(self.login_frame, "Password", font=("Arial", 12), show="*")
        self.password_entry.grid(row=3, column=1, padx=10, pady=5)

        # Bouton créer un compte
        self.create_account_button = tk.Button(self.login_frame, text="Create account", font=("Arial", 12), command=self.create_account)
        self.create_account_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        # Bouton se connecter
        self.login_button = tk.Button(self.login_frame, text="Login", font=("Arial", 12), command=self.login)
        self.login_button.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

    # Création de l'entrée texte
    def create_entry(self, parent, default_text, **kwargs):
        # Zones de textes
        entry = tk.Entry(parent, width=30, **kwargs)
        entry.default_text = default_text
        entry.insert(0, entry.default_text)
        entry.config(fg='grey')
        entry.bind("<FocusIn>", lambda event, entry=entry: self.entry_click_delete(event, entry))
        entry.bind("<FocusOut>", lambda event, entry=entry: self.entry_leave(event, entry))
        return entry

     # Efface le texte par défaut lorsqu'un champ de saisie est cliqué et change la couleur du texte
    def entry_click_delete(self, event, entry):
        if entry.get() == entry.default_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    # Rétablit le texte par défaut si le champ de saisie est vide lorsqu'il perd le focus, et change la couleur du texte
    def entry_click_restore(self, event, entry):
        if not entry.get():
            entry.insert(0, entry.default_text)
            entry.config(fg='grey')

    # Gère l'action lorsque le bouton "Create account" est cliqué
    def create_account(self):
        print("Create account in process")

    # Gère l'action lorsque le bouton "Login" est cliqué
    def login(self):
        print("Login in process")

if __name__ == "__main__":
    app = Login()
    app.mainloop()
