from PIL import Image
import numpy as np

def generate_key(image_shape):
    """Generate a random key matrix with the same shape as the image."""
    return np.random.randint(0, 256, size=image_shape, dtype=np.uint8)

def encrypt_image(image_path, key):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to a NumPy array
    img_array = np.array(img)

    # Ensure key has the same shape as img_array
    if key.shape != img_array.shape:
        raise ValueError("The key must have the same shape as the image.")

    # Encrypt each pixel using XOR with the key
    encrypted_array = np.bitwise_xor(img_array, key)
    
    # Convert the encrypted array back to an image
    encrypted_img = Image.fromarray(encrypted_array)
    
    # Save the encrypted image
    encrypted_img.save("encrypted_image.png")
    print("Image encrypted successfully as 'encrypted_image.png'.")


def decrypt_image(encrypted_image_path, key):
    # Open the encrypted image
    encrypted_img = Image.open(encrypted_image_path)
    
    # Convert the encrypted image to a NumPy array
    encrypted_array = np.array(encrypted_img)

    # Ensure key has the same shape as encrypted_array
    if key.shape != encrypted_array.shape:
        raise ValueError("The key must have the same shape as the encrypted image.")

    # Decrypt each pixel using XOR with the key
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    
    # Convert the decrypted array back to an image
    decrypted_img = Image.fromarray(decrypted_array)
    
    # Save the decrypted image
    decrypted_img.save("decrypted_image.png")
    print("Image decrypted successfully as 'decrypted_image.png'.")


def main():
    print("Enhanced Image Encryption and Decryption using Pixel Manipulation")

    # Loop to continuously ask for options until the user chooses to quit
    while True:
        # Prompt the user to select either encryption or decryption
        choice = input("Enter 'e' to encrypt an image, 'd' to decrypt an image, or 'q' to quit: ").lower()

        if choice == 'e':
            # Encrypt the image
            image_path = input("Enter the path to the image file: ")
            img = Image.open(image_path)
            img_array = np.array(img)
            
            # Generate a random key with the same shape as the image
            key = generate_key(img_array.shape)
            
            # Save the key to a file for future decryption (you can implement secure key storage)
            np.save("encryption_key.npy", key)
            
            encrypt_image(image_path, key)

        elif choice == 'd':
            # Decrypt the image
            encrypted_image_path = input("Enter the path to the encrypted image file: ")
            
            # Load the key from the saved file
            try:
                key = np.load("encryption_key.npy")
            except FileNotFoundError:
                print("Encryption key not found. Please encrypt an image first.")
                continue
            
            decrypt_image(encrypted_image_path, key)

        elif choice == 'q':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()

