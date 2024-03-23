
""" 
    This code is an implementation in Python that allows for the encryption of parameters using the cryptography library.
    There are two main functions, hash_Ap_params and encrypt_Com_params, which take in a list of parameters and encrypt certain ones.
    The encrypted values are added to a list encrypted_params and the encryption key is returned.
    The function save_Ap_params saves the encrypted parameters to a file named ectf_params.h in the application_processor/inc directory.
    The parameters are saved as macros defined in the file, where each macro is named after the parameter and the value is the encrypted equivalent of the parameter value.

    The function save_Comp_params is similar to save_Ap_params, but it saves the encrypted parameters to a file named ectf_params.h in the component/inc directory.

    The main loop waits for user input and calls the appropriate functions based on the command entered.
    If the command is ectf_build_ap, the parameters are encrypted with the function hash_Ap_params and saved to a file with the function save_Ap_params.
    If the command is ectf_build_component, the parameters are encrypted with the function encrypt_Com_params and saved to a file with the function save_Comp_params.

    The main goal of this code is to encrypt sensitive parameters to protect data and maintain the confidentiality of information.
    The encrypted parameters are then saved to specific files, which allows for their use in applications without compromising security.
"""
import subprocess
import shlex
import hashlib
import binascii
from wolfcrypt.ciphers import Aes, MODE_CBC
from ast import literal_eval
import os


def pad_message(plaintext):
    if len(plaintext) % 16 == 0:
        return plaintext
    return plaintext + (16 - (len(plaintext) % 16)) * chr(16 - (len(plaintext) % 16))

# Fonction pour chiffrer les paramètres
def hash_Ap_params(params):
    keyAP = ''
    # Chiffrer chaque paramètre séparément
    for i in range(len(params)):
        if(params[i] == '-c'):
            global component_cnt
            component_cnt = int(params[i+1])
        
        if(params[i] == '-ids'):
            global component_ids
            component_ids = params[i+1]
        
        if(params[i] == '-b'):
            global boot_message
            boot_message = str(params[i+1])
        
        if(params[i] == '-p'):
            global pin
            pin = params[i+1]
            pin = hashlib.sha1(pin.encode()).hexdigest()
              
        if(params[i] == '-t'):
            global token
            token = params[i+1]
            token = hashlib.sha1(token.encode()).hexdigest()
            
    return keyAP

# Générer le fichier ami partagé
def auth():
    with open("cat.h", "w") as file:
        file.write("\t //--------------------------------------------------\ \n")
        file.write("\t //|    CAT --- Colombe Academy of Technology ---   | \ \n")
        file.write("\t //|        ---   From Dakar, Senegal  ---          |  \ \n")
        file.write("\t //|  --- TaskForce Participating as 2024-CAT  ---  |  / \n")
        file.write("\t //|           ---Jom----Ngor----Fitt---            | / \n")
        file.write("\t //--------------------------------------------------/ \n")
        file.close()

def dethie(c,d,l,cle):
    with open("global_secrets.h", "w") as file:
        file.write(f"\t // /*'{c}'*/ \n")
        file.write(f"\t // /*'{d}'*/ \n")
        file.write(f"\t // /*'{l}'*/ \n")
        file.write(f"\t // /*{cle}*/ \n")
        file.close()


# Fonction pour enregistrer les paramètres chiffrés dans le fichier ectf_params.h
def save_Ap_params():
    with open("application_processor/ectf_params.h", "w") as file:
        file.write("#ifndef __ECTF_PARAMS__\n")
        file.write("#define __ECTF_PARAMS__\n")
        file.write("#define AP_PIN \"{}\"\n".format(pin))
        file.write("#define AP_TOKEN \"{}\"\n".format(token))
        file.write("#define COMPONENT_IDS {}\n".format(component_ids))
        file.write("#define COMPONENT_CNT {}\n".format(component_cnt))
        file.write("#define AP_BOOT_MSG \"{}\"\n".format(boot_message))
        file.write("#endif\n")
        file.close()

# Fonction pour chiffrer les paramètres des composants
def encrypt_Com_params(params):
    keyC = ''
    cipher = Aes(key="colombeAcademy-Taskforce", mode=MODE_CBC, IV="mitrEctf2024-cat")
    # Chiffrer chaque paramètre séparément
    for i in range(len(params)):
        if(params[i] == '-ad'):
            global attestation_date
            attestation_dateR = pad_message(params[i+1])
            attestation_dateH = cipher.encrypt(attestation_dateR)
            attestation_dateM = binascii.hexlify(attestation_dateH).decode()
            attestation_date=attestation_dateM[:15]
        
        if(params[i] == '-id'):
            global component_id
            component_id = literal_eval(params[i+1])
            
        if(params[i] == '-b'):
            global Comp_boot_message
            Comp_boot_message = params[i+1]
                
        if(params[i] == '-ac'):
            global attestation_customer
            attestation_customerR = pad_message(params[i+1])
            attestation_customerH = cipher.encrypt(attestation_customerR)
            attestation_customerM = binascii.hexlify(attestation_customerH).decode()
            attestation_customer=attestation_customerM[:15]
            
        if(params[i] == '-al'):
            global attestation_location
            attestation_locationR = pad_message(params[i+1])
            attestation_locationH = cipher.encrypt(attestation_locationR)
            attestation_locationM = binascii.hexlify(attestation_locationH).decode()
            attestation_location=attestation_locationM[:15]

    dethie(attestation_customerM,attestation_dateM,attestation_locationM,cipher._key)
    return keyC

# Fonction pour enregistrer les paramètres des composants chiffrés dans le fichier ectf_params.h
def save_Comp_params():
    with open("component/ectf_params.h", "w") as file:
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
auth()
# Et reculer pour quitter le deployment folder
os.chdir("..")

# Attendre la saisie utilisateur
command = input("Build your AP:")
params = shlex.split(command)

if(params[0] == "ectf_build_ap"):
    # Chiffrer les paramètres de la commande pour AP d'abord
    keyAP = hash_Ap_params(params)
    # Ensuite Enregistrer les paramètres chiffrés dans le fichier
    save_Ap_params()
    #---Et execute réellement sa commande build AP pour lui ici
    #l'autre AP_script ici
    subprocess.Popen('poetry run python3 deployment/Cp_Ap.py', shell=True)
    os.system(command)
    # Attendre la saisie à nouveau pour permettre de build les components
    command = input("AP built, Build Comp1:")
    params = shlex.split(command)
    for i in range(1,component_cnt):
        if(params[0] == "ectf_build_comp"):
            # Chiffrer les paramètres de la commande pour Components
            keyC = encrypt_Com_params(params)
            # Ensuite Enregistrer les paramètres chiffrés dans le fichier
            save_Comp_params()
            #--- Et enfin execute réellement sa commande build component ici pour lui
            #l'autre Comp_script ici
            subprocess.Popen('poetry run python3 deployment/Cp_Cp.py', shell=True)
            os.system(command)
            command = input("Done with Comp{}, build your comp{}:".format(i,i+1))
            params = shlex.split(command)
            keyC = encrypt_Com_params(params)
            # Enregistrer les paramètres chiffrés dans le fichier
            save_Comp_params()
            #--- execute réellement sa commande build component ici pour lui
            #l'autre Comp_script ici
            subprocess.Popen('poetry run python3 deployment/Cp_Cp.py', shell=True)
            os.system(command)

print("All Done !")
