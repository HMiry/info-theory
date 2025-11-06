import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def encrypt_ppm_file_ecb(input_file, output_file, key):
    """
    Encrypt the raw pixel data of a .ppm file with AES in ECB mode.
    """
    # 1. Read the .ppm header (first 4 lines).
    with open(input_file, 'rb') as f_in:
        h1 = f_in.readline()  # e.g., b'P6\n'
        h2 = f_in.readline()  # e.g., b'# CREATOR: GIMP...\n'
        h3 = f_in.readline()  # e.g., b'256 256\n'
        h4 = f_in.readline()  # e.g., b'255\n'
        header = h1 + h2 + h3 + h4
        plaintext = f_in.read()  # Remainder is pixel data
    
    # 2. Pad the plaintext to multiple of 16 bytes
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # 3. Set up AES in ECB mode
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # 4. Encrypt
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 5. Write the encrypted data + header
    #    Option A: Put the .ppm header *in front* of ciphertext
    with open(output_file, 'wb') as f_out:
        # If the instructions say to keep the header unencrypted, do:
        f_out.write(header)
        f_out.write(ciphertext)


def encrypt_ppm_file_cbc(input_file, output_file, key, iv):
    """
    Encrypt the raw pixel data with AES in CBC mode.
    """
    # 1. Read header + pixel data
    with open(input_file, 'rb') as f_in:
        h1 = f_in.readline()
        h2 = f_in.readline()
        h3 = f_in.readline()
        h4 = f_in.readline()
        header = h1 + h2 + h3 + h4
        plaintext = f_in.read()
    
    # 2. Padding
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # 3. Cipher setup
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 4. Write result
    with open(output_file, 'wb') as f_out:
        # Prepend the unencrypted header, followed by the IV if you wish
        f_out.write(header)
        f_out.write(ciphertext)


def encrypt_ppm_file_ctr(input_file, output_file, key, nonce):
    """
    Encrypt with AES in CTR mode.
    """
    # 1. Read header + pixel data
    with open(input_file, 'rb') as f_in:
        h1 = f_in.readline()
        h2 = f_in.readline()
        h3 = f_in.readline()
        h4 = f_in.readline()
        header = h1 + h2 + h3 + h4
        plaintext = f_in.read()
    
    # 2. Padding (CTR can handle arbitrary-length data, 
    #    but we often still pad for block alignment – or skip if not needed).
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    
    # 3. Set up AES in CTR mode
    #    The nonce typically is 8 bytes; the library will handle the rest of the counter bits.
    cipher = Cipher(
        algorithms.AES(key),
        modes.CTR(nonce),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    
    # 4. Encrypt
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    
    # 5. Write result
    with open(output_file, 'wb') as f_out:
        f_out.write(header)
        f_out.write(ciphertext)



def decrypt_ppm_file(encrypted_file, decrypted_file, key, mode, iv_or_nonce=None):
    with open(encrypted_file, 'rb') as f_in:
        # Read the same 4 lines (header)
        h1 = f_in.readline()
        h2 = f_in.readline()
        h3 = f_in.readline()
        h4 = f_in.readline()
        header = h1 + h2 + h3 + h4
        ciphertext = f_in.read()
    
    if mode == 'ECB':
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    elif mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv_or_nonce), backend=default_backend())
    elif mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv_or_nonce), backend=default_backend())
    else:
        raise ValueError("Unsupported mode")
    
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    
    # Unpad
    if mode != 'CTR':
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(plaintext) + unpadder.finalize()
    
    # Write out the recovered .ppm
    with open(decrypted_file, 'wb') as f_out:
        f_out.write(header)
        f_out.write(plaintext)

def compare_files(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        data1 = f1.read()
        data2 = f2.read()
    
    # Ensure both files are of the same length
    if len(data1) != len(data2):
        print("Files are of different lengths.")
        return
    
    # Count the number of differing bytes
    differing_bytes = sum(b1 != b2 for b1, b2 in zip(data1, data2))
    total_bytes = len(data1)
    
    print(f"Number of differing bytes: {differing_bytes}")
    print(f"Total bytes: {total_bytes}")
    print(f"Percentage of differing bytes: {differing_bytes / total_bytes * 100}%")


if __name__ == '__main__':
    # Example usage:
    # 128-bit key = 16 bytes
    key = os.urandom(16)
    
    # For CBC:
    iv = os.urandom(16)
    # For CTR:
    nonce = os.urandom(16)  # often 8 bytes is recommended; depends on library usage

    # % FIrst Part 

    ENCRIPTION_PATH = 'encryption'
    # make a directory for encryption
    os.makedirs(ENCRIPTION_PATH, exist_ok=True)
    # encrypt
    encrypt_ppm_file_ecb('Tux.ppm', os.path.join(ENCRIPTION_PATH, 'Tux_encr_ECB.ppm'), key)
    encrypt_ppm_file_cbc('Tux.ppm', os.path.join(ENCRIPTION_PATH, 'Tux_encr_CBC.ppm'), key, iv)
    encrypt_ppm_file_ctr('Tux.ppm', os.path.join(ENCRIPTION_PATH, 'Tux_encr_CTR.ppm'), key, nonce)
    print("Encryption complete! Examine Tux_encr_*.ppm to see results.")

    # decrypt 
    DECRIPTION_PATH = 'decryption'
    
    # make a directory for decryption
    os.makedirs(DECRIPTION_PATH, exist_ok=True)
    # Correct decryption
    decrypt_ppm_file(os.path.join(ENCRIPTION_PATH, 'Tux_encr_ECB.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_ECB.ppm'), key, 'ECB')
    decrypt_ppm_file(os.path.join(ENCRIPTION_PATH, 'Tux_encr_CBC.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_CBC.ppm'), key, 'CBC', iv)
    decrypt_ppm_file(os.path.join(ENCRIPTION_PATH, 'Tux_encr_CTR.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_CTR.ppm'), key, 'CTR', nonce)
    print("Decryption complete! Examine Tux_decr_*.ppm to see results.")

    # % Second Part : repeat the process for ECB mode. by changing 3 bits of the original key and compare the resulting encrypted image
    # 1. Change 3 bits of the key
    diff_key = bytearray(key)
    diff_key[0] ^= 0b00000111
    diff_key[1] ^= 0b00001111
    diff_key[2] ^= 0b00111111

    # 2. Encrypt the image with the modified key
    encrypt_ppm_file_ecb('Tux.ppm', os.path.join(ENCRIPTION_PATH, 'Tux_encr_ECB_modified.ppm'), bytes(diff_key))

    # 3. Compare the original and modified encrypted images
    with open(os.path.join(ENCRIPTION_PATH, 'Tux_encr_ECB.ppm'), 'rb') as f1:
        with open(os.path.join(ENCRIPTION_PATH, 'Tux_encr_ECB_modified.ppm'), 'rb') as f2:
            if f1.read() == f2.read():
                print('The original and modified encrypted images are the same')
            else:
                print('The original and modified encrypted images are different')

    # % Third Part :

    # Incorrect decryption

    # 1. FOR CBC MODe : Incorrect IV
    second_iv = os.urandom(16)
    decrypt_ppm_file(os.path.join(ENCRIPTION_PATH, 'Tux_encr_CBC.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_CBC_incorrect.ppm'), key, 'CBC', second_iv)

    # Compare the original and incorrect decrypted images
    print(58 * '-')
    print('Comparing the original and incorrect decrypted images for CBC mode')
    compare_files(os.path.join(DECRIPTION_PATH, 'Tux_decr_CBC.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_CBC_incorrect.ppm'))

    # 2. FOR CTR MODe : Incorrect nonce
    second_nonce = os.urandom(16)
    try:
        decrypt_ppm_file(os.path.join(ENCRIPTION_PATH, 'Tux_encr_CTR.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_CTR_incorrect.ppm'), key, 'CTR', second_nonce)
    except ValueError as e:
        print(f'Error: {e}')

    # Compare the original and incorrect decrypted images
    print(58 * '-')
    print('Comparing the original and incorrect decrypted images for CTR mode')
    compare_files(os.path.join(DECRIPTION_PATH, 'Tux_decr_CTR.ppm'), os.path.join(DECRIPTION_PATH, 'Tux_decr_CTR_incorrect.ppm'))

