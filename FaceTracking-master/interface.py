import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

class LoginInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("400x300")


        style = ttk.Style()
        style.configure("TLabel", padding=6, font=('Helvetica', 12))
        style.configure("TButton", padding=6, font=('Helvetica', 12))

        self.label_username = ttk.Label(root, text="Username:")
        self.label_username.pack(pady=6)

        self.entry_username = ttk.Entry(root)
        self.entry_username.pack(pady=6)

        self.label_password = ttk.Label(root, text="Password:")
        self.label_password.pack(pady=6)

        self.entry_password = ttk.Entry(root, show="*")
        self.entry_password.pack(pady=6)

        self.btn_login = ttk.Button(root, text="Login", command=self.login)
        self.btn_login.pack(pady=12)

    def login(self):
        # You can set up the authentication logic here
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Check the credentials
        if username == "aziz" and password == "aziz":
            self.run_hand_tracking()
        else:
            messagebox.showerror("Login Error", "Incorrect username or password")

    def run_hand_tracking(self):
        # Execute main.py using subprocess and wait for it to finish
        subprocess.run(["python", "main.py"])

        # Destroy the login window after the main program has completed
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    login_interface = LoginInterface(root)
    root.mainloop()
