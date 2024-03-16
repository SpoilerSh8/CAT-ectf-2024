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