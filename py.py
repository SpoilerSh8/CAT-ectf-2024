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



# propose une implementation correcte des fonctions:secure_send(), secure_receive(), get_provisioned_ids() pour assurer une communication post boot sécuriser entre l'application processor et les differents composants. s'il le faut meme ajouter un systeme de partage de clés pour assurer l'authenticité de l'AP et de components. et propose aussi ce qu'on doit implementer du coté des fichiers board_link impliqués et des components pour que cela correspond
# 1-
# The secure_send() function should encrypt the data before sending it to the component. We can use AES encryption for this purpose. Here is a possible implementation:
# int secure_send(uint8_t address, uint8_t* buffer, uint8_t len) {
#     // Generate a random encryption key
#     uint8_t key[AES_BLOCK_SIZE];
#     generate_random_key(key);

#     // Encrypt the data using AES encryption
#     uint8_t encrypted_data[len];
#     aes_encrypt(buffer, encrypted_data, key);

#     // Send the encrypted data over I2C
#     int sent = send_packet(address, len, encrypted_data);
#     if (sent == ERROR_RETURN) {
#         print_error("Error sending data over I2C: %d\n", sent);
#     }
#     return sent;
# }


# 2-The secure_receive() function should authenticate the data received from the component. We can use AES encryption with a shared key for this purpose. Here is a possible implementation:
# int secure_receive(i2c_addr_t address, uint8_t* buffer) {
#     // Receive the data over I2C
#     int received = poll_and_receive_packet(address, buffer);
#     if (received == ERROR_RETURN) {
#         print_error("Error receiving data over I2C: %d\n", received);
#         return ERROR_RETURN;
#     }

#     // Decrypt the data using AES encryption
#     uint8_t decrypted_data[received];
#     aes_decrypt(buffer, decrypted_data, key);

#     // Verify the integrity of the data
#     if (verify_integrity(decrypted_data)) {
#         print_error("Error verifying data integrity: invalid AES key\n");
#         return ERROR_RETURN;
#     }

#     // Copy the decrypted data to the output buffer
#     memcpy(buffer, decrypted_data, received);
#     return received;
# }

# 3-
# The get_provisioned_ids() function should return the provisioned IDs of the components. We can add a shared key to authenticate the AP with the components. Here is a possible implementation:
# int get_provisioned_ids(uint32_t* buffer) {
#     // Verify the shared key with the AP
#     if (!verify_shared_key()) {
#         print_error("Error verifying shared key with AP\n");
#         return ERROR_RETURN;
#     }

#     // Copy the provisioned IDs to the output buffer
#     memcpy(buffer, flash_status.component_ids, flash_status.component_cnt * sizeof(uint32_t));
#     return flash_status.component_cnt;
# }

# 4-Key Sharing Mechanism:
# To share the key between the AP and the components, we can use a symmetric key encryption algorithm like AES. We can use the following steps to share the key:

# The AP generates a random AES key and stores it in the flash memory.
# The AP shares the key with the components using a secure channel.
# The components store the shared key in their non-volatile memory.
# To ensure the security of the key, we can use a secure communication channel like SSL/TLS or SSH to share the key. We can also use a public-key encryption algorithm like RSA or ECC to securely share the key.

# Board Link Implementation:
# The board_link.h and board_link.c files should be modified to include the secure communication functions. Here are the suggested changes:

# Add a function to initialize the secure communication channel.
# Add a function to send encrypted data over the I2C interface.
# Add a function to receive encrypted data over the I2C interface.

# 5-Sure, here are the proposed changes to the board_link files to include the secure communication functions:

# board_link.h:

# Add the following function prototypes:
# int board_link_init(void);
# int secure_send(uint8_t address, uint8_t* buffer, uint8_t len);
# int secure_receive(i2c_addr_t address, uint8_t* buffer, uint8_t len);

# board_link.c:

# Implement the following functions:

# 1-board_link_init:
# Initialize the I2C interface and the flash memory.
# int board_link_init(void) {
#     // Initialize the I2C interface
#     if (i2c_init() < 0) {
#         print_error("Error initializing I2C\n");
#         return ERROR_RETURN;
#     }

#     // Initialize the flash memory
#     if (flash_init() < 0) {
#         print_error("Error initializing flash memory\n");
#         return ERROR_RETURN;
#     }

#     return SUCCESS_RETURN;
# }

# 2-secure_send:
# Encrypt the data using the AES encryption algorithm and send it over the I2C interface.
# int secure_send(uint8_t address, uint8_t* buffer, uint8_t len) {
#     // Generate a random encryption key
#     uint8_t key[AES_BLOCK_SIZE];
#     generate_random_key(key);

#     // Encrypt the data using AES encryption
#     uint8_t encrypted_data[len];
#     aes_encrypt(buffer, encrypted_data, key);

#     // Send the encrypted data over I2C
#     int sent = send_packet(address, len, encrypted_data);
#     if (sent == ERROR_RETURN) {
#         print_error("Error sending data over I2C: %d\n", sent);
#     }
#     return sent;
# }

# 3-secure_receive:
# Receive the encrypted data over the I2C interface and decrypt it using the AES encryption algorithm.
# int secure_receive(i2c_addr_t address, uint8_t* buffer, uint8_t len) {
#     // Receive the encrypted data over I2C
#     int received = poll_and_receive_packet(address, buffer);
#     if (received == ERROR_RETURN) {
#         print_error("Error receiving data over I2C: %d\n", received);
#         return ERROR_RETURN;
#     }

#     // Decrypt the data using the AES encryption algorithm
#     uint8_t decrypted_data[received];
#     aes_decrypt(buffer, decrypted_data, key);

#     // Copy the decrypted data to the output buffer
#     memcpy(buffer, decrypted_data, received);
#     return received;
# }
# Note that the key used for encryption and decryption is assumed to be shared securely between the AP and the components.

# 6- In this case, one way to share the encryption key securely is to use a symmetric key encryption algorithm like AES. We can use the following steps to share the key:

# The AP generates a random encryption key and stores it in the flash memory.
# The AP sends the encrypted key to the component using the secure_send() function.
# The component decrypts the key using the corresponding decryption key.
# The component stores the decrypted key in its non-volatile memory.
# Here is an example of how to share the encryption key securely over the I2C interface using the secure_send() and secure_receive() functions:

# In the AP-side code:

# int share_key_securely(i2c_addr_t component_address) {
#     uint8_t key[AES_KEY_SIZE];
#     uint8_t encrypted_key[AES_KEY_SIZE];

#     // Generate a random encryption key
#     generate_random_key(key);

#     // Encrypt the encryption key using the component's public key
#     encrypt_key(key, encrypted_key);

#     // Send the encrypted key to the component
#     secure_send(component_address, encrypted_key, AES_KEY_SIZE);

#     return SUCCESS_RETURN;
# }
# In the component-side code:

# int receive_key_securely(i2c_addr_t ap_address) {
#     uint8_t encrypted_key[AES_KEY_SIZE];
#     uint8_t key[AES_KEY_SIZE];

#     // Receive the encrypted key from the AP
#     secure_receive(ap_address, encrypted_key, AES_KEY_SIZE);

#     // Decrypt the encrypted key using the private key
#     decrypt_key(encrypted_key, key);

#     // Store the decrypted key in the component's non-volatile memory
#     store_key_in_memory(key);

#     return SUCCESS_RETURN;
# }

# Note that in this example, we assume that the AP and the components have a public-private key pair and the corresponding public key is known to the other party. The encrypt_key() and decrypt_key() functions are implemented using the public key encryption algorithm.






















ectf_build_ap -d . -on ap -p 123456 -c 2 -ids "0x11111111, 0x11111112" -b "boot ap" -t 0123456789abcdef -od build 
ectf_build_comp -d . -on comp1 -od build -id 0x11111111 -b "boot comp1"  -al "Dakar" -ad "02/02/24" -ac "Fatou"    
ectf_build_comp -d . -on comp2 -od build -id 0x11111112 -b "boot comp2"  -al "Dakar" -ad "02/02/24" -ac "sokhna"

# TimeoutError
# To add a timeout mechanism to the existing code so that if a response to a command (attest, list, etc.) is not received within 3 seconds, the communication is interrupted, you can follow these steps:
# 1-Introduce a new delay function that accepts time in milliseconds.
# void mxc_delay(uint32_t milliseconds) {
#     MXC_Delay(milliseconds * 1000);
# }

#2- Implement a function for setting timeout and interrupting the communication.
# enum TimeoutResult {
#     NOT_TIMEDOUT,
#     TIMEDOUT,
#     COMM_ERROR
# };

# enum TimeoutResult issue_cmd_with_timeout(i2c_addr_t addr, uint8_t* transmit, uint8_t* receive, uint32_t timeout_ms) {
#     int len = issue_cmd(addr, transmit, receive);
#     if (len == ERROR_RETURN) {
#         return COMM_ERROR;
#     }
#     if (len > 0) {
#         return NOT_TIMEDOUT;
#     }
#     // Wait until timeout or response arrives
#     uint32_t start = mxc_millis();
#     while (!len && ((uint32_t)(mxc_millis() - start) < timeout_ms)) {
#         mxc_delay(10);
#         len = poll_and_receive_packet(addr, receive);
#     }
#     if (len > 0) {
#         return NOT_TIMEDOUT;
#     }
#     if ((uint32_t)(mxc_millis() - start) < timeout_ms) {
#         return TIMEDOUT;
#     }
#     return COMM_ERROR;
# }

# 3- Replace any call to issue_cmd in the provided code to issue_cmd_with_timeout with a 3000 (3 seconds) timeout.
# For example, replace the function call given below:
# int len = issue_cmd(addr, transmit_buffer, receive_buffer);
# with:
# enum TimeoutResult result = issue_cmd_with_timeout(addr, transmit_buffer, receive_buffer, 3000);
# if (result == NOT_TIMEDOUT) {
#     // Process the result here
#     len = receive_buffer;
# } else {
#     // Handle the error (either TIMEDOUT or COMM_ERROR)
#     print_error("Timeout or communication error while issuing '%s' command", commands[i].name);
#     return EXIT_FAILURE;
# }