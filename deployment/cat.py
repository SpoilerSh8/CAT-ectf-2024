import subprocess
from cryptography.fernet import Fernet

# Fonction pour chiffrer les paramètres
def encrypt_params(params):
    # Clé de chiffrement
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    
    encrypted_params = []
    # Chiffrer chaque paramètre séparément
    for param in params:
        encrypted_param = cipher_suite.encrypt(param.encode())
        encrypted_params.append(encrypted_param)
    
    return encrypted_params, key

# Fonction pour enregistrer les paramètres chiffrés dans le fichier ectf_params.h
def save_params_to_file(params, key):
    with open('ectf_params.h', 'wb') as file:
        file.write(b'#ifndef ECTF_PARAMS_H\n#define ECTF_PARAMS_H\n\n')
        file.write(b'const char *encrypted_params[] = {\n')
        for param in params:
            file.write(b'\t"')
            file.write(param)
            file.write(b'",\n')
        file.write(b'};\n')
        file.write(b'#endif\n')
    # Empêcher l'écrasement du fichier
    subprocess.run(['chmod', '400', 'ectf_params.h'])

# Boucle principale pour attendre les saisies utilisateur
while True:
    # Attendre la saisie utilisateur
    command = input(" ")
    
    # Vérifier si une commande a été saisie
    if command:
        # Séparer les paramètres de la commande
        params = command.split()
        
        # Chiffrer les paramètres de la commande
        encrypted_params, key = encrypt_params(params)
        
        # Enregistrer les paramètres chiffrés dans le fichier
        save_params_to_file(encrypted_params, key)
        
        print("Parameters encrypted and saved in ectf_params.h. Waiting for next command...")

