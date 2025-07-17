import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from Crypto.Cipher import AES

NONCE_SIZE = 8
FOOTER_SIZE = 69

class DjvuDecryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulated STOP Djvu Decryptor")
        self.directory = ""
        self.key = b""
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Clé AES (hex) :").grid(row=0, column=0, sticky="w")
        self.key_entry = tk.Entry(self.root, width=70)
        self.key_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Button(self.root, text="📁 Choisir Dossier", command=self.select_directory).grid(row=1, column=0, pady=5)
        self.dir_label = tk.Label(self.root, text="Aucun dossier sélectionné", anchor="w")
        self.dir_label.grid(row=1, column=1, sticky="w")

        tk.Button(self.root, text="🔓 Déchiffrer", command=self.decrypt_all).grid(row=2, column=0, pady=5)
        self.output = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.output.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def log(self, msg):
        self.output.insert(tk.END, msg + "\n")
        self.output.see(tk.END)
        print(msg)

    def select_directory(self):
        self.directory = filedialog.askdirectory()
        if self.directory:
            self.dir_label.config(text=self.directory)

    def decrypt_file(self, path):
        try:
            with open(path, 'rb') as f:
                data = f.read()
            if len(data) < NONCE_SIZE + FOOTER_SIZE:
                self.log(f"[-] Trop court ou non valide : {os.path.basename(path)}")
                return
            nonce = data[:NONCE_SIZE]
            ciphertext = data[NONCE_SIZE:-FOOTER_SIZE]
            cipher = AES.new(self.key, AES.MODE_CTR, nonce=nonce)
            plaintext = cipher.decrypt(ciphertext)

            out_path = path.rsplit('.', 1)[0]
            with open(out_path, 'wb') as f:
                f.write(plaintext)

            self.log(f"[+] Déchiffré : {os.path.basename(path)}")
        except Exception as e:
            self.log(f"[!] Échec : {os.path.basename(path)} ({e})")

    def decrypt_all(self):
        key_hex = self.key_entry.get().strip()
        if len(key_hex) != 64:
            messagebox.showerror("Erreur", "La clé AES doit être de 64 caractères hex.")
            return
        try:
            self.key = bytes.fromhex(key_hex)
        except:
            messagebox.showerror("Erreur", "Clé hexadécimale invalide.")
            return

        if not self.directory:
            messagebox.showerror("Erreur", "Veuillez sélectionner un dossier.")
            return

        self.output.delete("1.0", tk.END)
        self.log(f"[i] Déchiffrement du dossier : {self.directory}")
        for file in os.listdir(self.directory):
            if file.endswith(".zzla"):
                self.decrypt_file(os.path.join(self.directory, file))
        self.log("[✓] Terminé.")

# Lancement
if __name__ == "__main__":
    root = tk.Tk()
    app = DjvuDecryptorApp(root)
    root.mainloop()
