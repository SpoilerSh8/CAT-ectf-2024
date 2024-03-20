# import binascii

# from wolfcrypt.ciphers import Aes, MODE_CBC

# cipher = Aes(key="colombeAcademy-Taskforce", mode=MODE_CBC, IV="mitrEctf2024-cat")
# plaintext = 'e0c9c858312ca472b76525d287a050a8'
# print(f"Plaintext: {plaintext}")

# # Encryption
# ctext = cipher.encrypt(plaintext)
# print(f"Ciphertext (Raw): {ctext}")

# # Convert ciphertext to hexadecimal format
# ctext_hex = binascii.hexlify(ctext).decode()
# print(f"Ciphertext (Hex): {ctext_hex}")

# # Decryption
# dtext = cipher.decrypt(binascii.unhexlify('373aed4a56b98d79050f8746956e3569'))
# print(f"DeCiphertext: {dtext}")
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

#7c4a8d09ca3762af61e59520943dc26494f8941b


# void print_hash_result(uint8_t* hash_result) {
#     char hash_str[41]; // +1 pour le caractère nul de fin de chaîne
#     for (int i = 0; i < 20; i++) {
#         char hex[3];
#         sprintf(hex, "%02x", hash_result[i]);
#         strncat(hash_str, hex, 2);
#     }
#     print_info("Hash result: %s\n", hash_str);
# }

// Limit the number of failed PIN attempts to prevent brute force attacks
#define MAX_FAILED_PIN_ATTEMPTS 5

// Define the maximum delay counter value
#define MAX_DELAY_COUNTER 1

// Initialize the number of failed PIN attempts and the delay counter
int failed_pin_attempts = 0;
int delay_counter = 0;

    failed_pin_attempts++;

    // If the maximum number of failed PIN attempts is reached, lock the account and add a delay
    if (failed_pin_attempts >= MAX_FAILED_PIN_ATTEMPTS) {
        print_error("Too many failed PIN attempts, account locked!\n");
        // Add code to lock the account here
        // Add a 5-second delay before becoming fully functional again
        while (delay_counter < MAX_DELAY_COUNTER) {
            delay(5);
            delay_counter++;
        }
        delay_counter = 0;
    }
    return ERROR_RETURN;
}


// Function to delay for a certain amount of time
void delay(int seconds) {
    // Get the current time
    clock_t start_time = clock();

    // Loop until the desired amount of time has passed
    while ( (clock() - start_time) / CLOCKS_PER_SEC < seconds);
}