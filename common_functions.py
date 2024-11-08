from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def aes_encrypt(plaintext, key):
    plaintext = pad(plaintext)
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext.encode())

def create_unique_id(index, aes_key):
    id_start = 'S628'
    plaintext = f'{index}'.zfill(7)
    encrypted = aes_encrypt(plaintext, aes_key)
    hex_encrypted = encrypted.hex()
    id_end = hex_encrypted[:7].upper()
    unique_id = f'{id_start}{id_end}'
    return unique_id
