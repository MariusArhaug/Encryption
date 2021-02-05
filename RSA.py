"""Modules"""
import random
from math import gcd
# from numpy import power
from Cipher import Cipher
from crypto_utils import generate_random_prime, modular_inverse, blocks_from_text, text_from_blocks


class RSA(Cipher):
    """Subclass of Cipher"""
    def __init__(self, bits=8, length=1):
        self.__bits__ = bits
        self.__length__ = length

    def encode(self, clear_text, key):
        """
        Encrypt message with public key.
        Change the cleartext into a binary number
        then change it into blocks of integers
        :param clear_text: clear message
        :param key: public key (n,e) to encrypt
        :return: list of integers "c", where c = pow(t, e, n)
        """
        n, e = key

        # For every char in clear_text change into ascii value
        # and change that into 8 bit binary, then concat
        binary_message = "".join(f"{ord(char):08b}" for char in clear_text.upper())
        # Get list of integers from binary_message
        int_list = blocks_from_text(binary_message, self.__length__)
        encrypted_message = []
        for t_int in int_list:
            c_encrypted = pow(t_int, e, n)
            encrypted_message.append(c_encrypted)
        return encrypted_message

    def decode(self, encoded_text, key):
        """
        Decode message using private key
        :param encoded_text: encoded list of integers "c"s
        :param key: private key (n,d) used to decrypt
        :return: decrypted message
        """
        n, d = key
        decrypted_integers = []
        for c_encrypted in encoded_text:
            t_prime = pow(c_encrypted, d, n)
            decrypted_integers.append(t_prime)

        binary_message = text_from_blocks(decrypted_integers, self.__bits__)
        decrypted_message = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        decrypted_message = "".join([chr(int(x, 2)) for x in decrypted_message])

        return decrypted_message

    def generate_keys(self):
        """
        Generate keys for sender and receiver
        :return: key_one is for sender and key_two is for receiver
        """
        while True:
            prime_p = generate_random_prime(self.__bits__)
            prime_q = generate_random_prime(self.__bits__)
            if prime_p != prime_q:
                break
        n = prime_p*prime_q
        theta = (prime_p-1)*(prime_q-1)

        while True:
            e = random.randint(3, theta-1)
            if gcd(e, theta) == 1:
                break
        d = modular_inverse(e, theta)

        key_encrypt = (n, e)
        key_decrypt = (n, d)
        return key_encrypt, key_decrypt

    def possible_keys(self):
        return 'inf'
