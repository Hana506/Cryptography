# import des cipher algorithm from crypto library
from Crypto.Cipher import DES
# import padding functions to make text fit block size
from Crypto.Util.Padding import pad, unpad
# import base64 to encode encrypted data as readable text
import base64

def encrypt_des(plain_text, key):
    # check if key is exactly 8 characters long
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long")
    
    # create a new des cipher object with the key
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    # pad the text to match des block size (8 bytes)
    padded_text = pad(plain_text.encode('utf-8'), DES.block_size)
    # encrypt the padded text
    encrypted = cipher.encrypt(padded_text)
    # convert encrypted bytes to base64 string for display
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_des(cipher_text, key):
    # check if key is exactly 8 characters long
    if len(key) != 8:
        raise ValueError("Key must be exactly 8 bytes long")
    
    # create a new des cipher object with the same key
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)
    # decode the base64 string back to encrypted bytes
    encrypted = base64.b64decode(cipher_text)
    # decrypt the encrypted bytes
    decrypted = cipher.decrypt(encrypted)
    # remove the padding from decrypted text
    unpadded = unpad(decrypted, DES.block_size)
    # convert bytes back to string
    return unpadded.decode('utf-8')

def main():
    # print header with decoration
    print("=" * 50)
    print("DES Encryption/Decryption Program")
    print("=" * 50)
    
    # main loop to keep program running
    while True:
        # show menu options to user
        print("\nChoose an option:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        # get user choice and remove extra spaces
        choice = input("\nEnter your choice (1/2/3): ").strip()
        
        # if user chose encryption
        if choice == '1':
            print("\n--- ENCRYPTION ---")
            # get the text to encrypt
            plain_text = input("Enter the plain text: ")
            # get the secret key
            key = input("Enter the key (exactly 8 characters): ")
            
            # validate key length again
            if len(key) != 8:
                print("Error: Key must be exactly 8 characters long!")
                continue
            
            # try to encrypt and handle any errors
            try:
                cipher_text = encrypt_des(plain_text, key)
                print(f"\nCipher Text: {cipher_text}")
            except Exception as e:
                print(f"Error: {e}")
        
        # if user chose decryption
        elif choice == '2':
            print("\n--- DECRYPTION ---")
            # get the encrypted text
            cipher_text = input("Enter the cipher text: ")
            # get the secret key used for encryption
            key = input("Enter the key (exactly 8 characters): ")
            
            # validate key length again
            if len(key) != 8:
                print("Error: Key must be exactly 8 characters long!")
                continue
            
            # try to decrypt and handle any errors
            try:
                plain_text = decrypt_des(cipher_text, key)
                print(f"\nPlain Text: {plain_text}")
            except Exception as e:
                print(f"Error: {e}")
        
        # if user chose to exit
        elif choice == '3':
            print("\nExiting program. Goodbye!")
            break
        
        # if user entered invalid choice
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")

# run the main function when script is executed
if __name__ == "__main__":
    main()
