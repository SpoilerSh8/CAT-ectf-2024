import binascii

from wolfcrypt.ciphers import Aes, MODE_CBC

cipher = Aes(key="colombeAcademy-Taskforce", mode=MODE_CBC, IV="mitrEctf2024-cat")
plaintext = 'e0c9c858312ca472b76525d287a050a8'
print(f"Plaintext: {plaintext}")

# Encryption
ctext = cipher.encrypt(plaintext)
print(f"Ciphertext (Raw): {ctext}")

# Convert ciphertext to hexadecimal format
ctext_hex = binascii.hexlify(ctext).decode()
print(f"Ciphertext (Hex): {ctext_hex}")

# Decryption
dtext = cipher.decrypt(binascii.unhexlify('373aed4a56b98d79050f8746956e3569'))
print(f"DeCiphertext: {dtext}")
#
# import binascii
# from wolfcrypt.ciphers import Aes, MODE_CBC

# cipher = Aes(key="colombeAcademy-Taskforce", mode=MODE_CBC, IV="mitrEctf2024-cat")

# plaintext = '0123456789abcdef'
# plaintext = input(f"Plaintext: {plaintext}\nEnter your message (any size): ")

# # Add padding if required
# def pad_message(plaintext):
#     if len(plaintext) % 16 == 0:
#         return plaintext
#     return plaintext + (16 - (len(plaintext) % 16)) * chr(16 - (len(plaintext) % 16))

# padded_plaintext = pad_message(plaintext)

# print(f"Padded plaintext: {padded_plaintext}")

# # Encryption
# ctext = cipher.encrypt(padded_plaintext)
# print(f"Ciphertext (Raw): {ctext}")

# # Convert ciphertext to hexadecimal format
# ctext_hex = binascii.hexlify(ctext).decode()
# print(f"Ciphertext (Hex): {ctext_hex}")

# # Decryption
# unpadded_dtext = cipher.decrypt(ctext)

# def strip_padding(padded_text):
#     return padded_text.rstrip(padded_text[-1])

# dtext = strip_padding(unpadded_dtext)

# print(f"DeCiphertext: {dtext}")


# ectf_build_ap -d . -on ap -p 123456 -c 2 -ids "0x11111111, 0x11111112" -b "boot ap" -t 0123456789abcdef -od build
# ectf_build_comp -d . -on comp1 -od build -id 0x11111111 -b "boot comp1"  -al "Dakar" -ad "02/02/24" -ac "Fatou"
# ectf_build_comp -d . -on comp2 -od build -id 0x11111112 -b "boot comp2"  -al "Dakar" -ad "02/02/24" -ac "sokhna"




#To check


# est ce que vous avez compris ? genre je veux utliser la meme fonction pour hashage qui a été utilisée en python, je veux utiliser la meme dans mo fichier application processor qui est lui en C. de telle sorte que quad je vais hasher le pin il va correspodre exactement à celui qui est généré par le fichier python et qui est stocké dans AP_PIN tout ça en utilisant wolfssl


# Je comprends mieux maintenant ce que vous souhaitez réaliser. Vous aimeriez utiliser la même fonction de hachage dans votre fichier application_processor.c en C, afin que le hachage de pin corresponde exactement à celui généré par le script Python et stocké dans AP_PIN, en utilisant wolfSSL.

# Malheureusement, la bibliothèque wolfSSL ne propose pas d'implémentation de HmacSha directement utilisable, elle propose une variété d'algorithmes de hachage, mais je vais vous montrer comment mettre en œuvre une fonction de hachage personnalisée en utilisant l'algorithme SHA-256 de wolfSSL. De cette manière, vous obtiendrez des résultats hashés similaires à ceux du script Python, qui utilise le module wolfcrypt.hashes et l'algorithme HMAC-SHA-256.

# Tout d'abord, vous devez inclure la bibliothèque wolfSSL dans votre projet C et l'initialiser.

# Vous pouvez créer une fonction hash_pin dans votre fichier application_processor.c qui hache le pin :
# #include <string.h>
# #include <wolfssl/options.h>
# #include <wolfssl/ssl.h>
# #include <wolfssl/sha.h>

# // Initialise le contexte de hachage
# void InitHashContext(WolfSSL_Hash_ctx *ctx, const char *key)
# {
#     wc_Sha256 sha256;
#     wc_InitSha256(&sha256);

#     // Remplacez 'key' par la clé Python utilisée dans votre script (par ex. : "cleAP").
#     wc_Sha256Update(&sha256, (const unsigned char*)key, strlen(key));

#     *ctx = sha256;
# }

# // Effectue le hachage
# int HashPin(const char *pin, WolfSSL_Hash_ctx *ctx, unsigned char *result)
# {
#     size_t taille_donnees_hachees;

#     wc_Sha256Update(ctx, (const unsigned char*)pin, strlen(pin));

#     wc_Sha256Final(ctx, result, &taille_donnees_hachees);

#     return 0;
# }

# // Utilisez ces fonctions dans votre application_processor.c, de la manière suivante :
# int main(int argc, char *argv[])
# {
#     WolfSSL_Hash_ctx ctx;
#     unsigned char result[WC_SHA256_DIGEST_SIZE];

#     InitHashContext(&ctx, "cleAP");

#     if (hash_pin("mon_pin_secret", &ctx, result) == 0)
#     {
#         // Utilisez 'result' pour effectuer les comparaisons avec 'AP_PIN'
#     }

#     return 0;
# }