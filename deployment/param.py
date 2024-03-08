
""" 
    This code is an implementation in Python that allows for the encryption of parameters using the cryptography library.
    There are two main functions, encrypt_Ap_params and encrypt_Com_params, which take in a list of parameters and encrypt certain ones.
    The encrypted values are added to a list encrypted_params and the encryption key is returned.
    The function save_Ap_params saves the encrypted parameters to a file named ectf_params.h in the application_processor/inc directory.
    The parameters are saved as macros defined in the file, where each macro is named after the parameter and the value is the encrypted equivalent of the parameter value.

    The function save_Comp_params is similar to save_Ap_params, but it saves the encrypted parameters to a file named ectf_params.h in the component/inc directory.

    The main loop waits for user input and calls the appropriate functions based on the command entered.
    If the command is ectf_build_ap, the parameters are encrypted with the function encrypt_Ap_params and saved to a file with the function save_Ap_params.
    If the command is ectf_build_component, the parameters are encrypted with the function encrypt_Com_params and saved to a file with the function save_Comp_params.

    The main goal of this code is to encrypt sensitive parameters to protect data and maintain the confidentiality of information.
    The encrypted parameters are then saved to specific files, which allows for their use in applications without compromising security.
"""

import shlex
from cryptography.fernet import Fernet
import os

# Fonction pour chiffrer les paramètres
def encrypt_Ap_params(params):
    # Clé de chiffrement
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_params = []
    # Chiffrer chaque paramètre séparément
    for i in range(len(params)):
        if(params[i] == '-c'):
            global component_cnt
            component_cnt = int(params[i+1])
        
        if(params[i] == '-ids'):
            global component_ids
            component_ids = (params[i+1])
        
        if(params[i] == '-b'):
            global boot_message
            boot_message = str(params[i+1])
        
        if(params[i] == '-p'):
            global pin
            pin = params[i+1]
            encrypted_param = cipher_suite.encrypt(params[i+1].encode())
            pin=encrypted_param
              
        if(params[i] == '-t'):
            global token
            token = params[i+1]
            encrypted_param = cipher_suite.encrypt(params[i+1].encode())
            token=encrypted_param
            
    return encrypted_params, key


# Fonction pour enregistrer les paramètres chiffrés dans le fichier ectf_params.h
def save_Ap_params():
    with open("application_processor/inc/ectf_params.h", "w") as file:
        file.write("#ifndef __ECTF_PARAMS__\n")
        file.write("#define AP_PIN \"{}\"\n".format(pin))
        file.write("#define AP_TOKEN \"{}\"\n".format(token))
        file.write("#define COMPONENT_IDS {}\n".format(component_ids))
        file.write("#define COMPONENT_CNT {}\n".format(component_cnt))
        file.write("#define AP_BOOT_MSG \"{}\"\n".format(boot_message))
        file.write("#endif\n")
        file.close()
    # Empêcher l'écrasement du fichier
    # subprocess.run(['chmod', '400', 'application_processor/inc/ectf_params.h'])

# Fonction pour chiffrer les paramètres des composants
def encrypt_Com_params(params):
    # Clé de chiffrement
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_params = []
    # Chiffrer chaque paramètre séparément
    for i in range(len(params)):
        if(params[i] == '-ad'):
            global attestation_date
            attestation_date = params[i+1]
            encrypted_param = cipher_suite.encrypt(params[i+1].encode())
            attestation_date=encrypted_param
            
        if(params[i] == '-id'):
            global component_id
            component_id = (params[i+1])
            
        if(params[i] == '-b'):
            global Comp_boot_message
            Comp_boot_message = (params[i+1])
                
        if(params[i] == '-ac'):
            global attestation_customer
            attestation_customer = params[i+1]
            encrypted_param = cipher_suite.encrypt(params[i+1].encode())
            attestation_customer=encrypted_param
            encrypted_params.append(encrypted_param)
            
        if(params[i] == '-al'):
            global attestation_location
            attestation_location = params[i+1]
            encrypted_param = cipher_suite.encrypt(params[i+1].encode())
            attestation_location=encrypted_param
            encrypted_params.append(encrypted_param)
     
    return encrypted_params, key

# Fonction pour enregistrer les paramètres des composants chiffrés dans le fichier ectf_params.h
def save_Comp_params():
    with open("component/inc/ectf_params.h", "w") as file:
        file.write("#ifndef _ECTF_PARAMS_\n")
        file.write("#define _ECTF_PARAMS_\n")
        file.write("#define COMPONENT_ID {}\n".format(component_id))
        file.write("#define COMPONENT_BOOT_MSG \"{}\"\n".format(Comp_boot_message))
        file.write("#define ATTESTATION_LOC \"{}\"\n".format(attestation_location))
        file.write("#define ATTESTATION_DATE \"{}\"\n".format(attestation_date))
        file.write("#define ATTESTATION_CUSTOMER \"{}\"\n".format(attestation_customer))
        file.write("#endif\n")
        file.close()

# ----------------------------- Main de l'application ---------------------------------
# Générer le fichier jeton partagé
with open("hello.h", "w") as file:
        file.write("\t #define CAT '--- Colombe Academy of Technology ---'\n")
        file.write("\t #define CAT1 '---     From Dakar, Senegal  ---'\n")
        file.write("\t #define CAT2 '---   Participating as 2024-CAT   ---'\n")
        file.close()
# Et reculer pour quitter le deployment folder
os.chdir("..")

# Attendre la saisie utilisateur
command = input("Build your AP:")
params = shlex.split(command)

if(params[0] == "ectf_build_ap"):
    # Chiffrer les paramètres de la commande pour AP d'abord
    encrypted_params, key = encrypt_Ap_params(params)
    # Ensuite Enregistrer les paramètres chiffrés dans le fichier
    save_Ap_params()
    #---Et execute réellement sa commande build AP pour lui ici
    os.system(command)
    # Attendre la saisie à nouveau pour permettre de build les components
    command = input("Build Comp1:")
    params = shlex.split(command)
    for i in range(1,component_cnt):
        if(params[0] == "ectf_build_comp"):
            # Chiffrer les paramètres de la commande pour Components
            encrypted_params, key = encrypt_Com_params(params)
            # Ensuite Enregistrer les paramètres chiffrés dans le fichier
            save_Comp_params()
            #--- Et enfin execute réellement sa commande build component ici pour lui
            os.system(command)
            command = input("Done with Comp{}, build your comp{}:".format(i,i+1))
            params = shlex.split(command)
            encrypted_params, key = encrypt_Com_params(params)
            # Enregistrer les paramètres chiffrés dans le fichier
            save_Comp_params()
            #--- execute réellement sa commande build component ici pour lui
            os.system(command)

print("all Done !")


