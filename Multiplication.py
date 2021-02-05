"""
Multiplication cipher
"""
from Caesar import Caesar, Cipher, random
from crypto_utils import modular_inverse
from math import gcd


class Multiplication(Caesar):

    def encode(self, clear_text, key):
        """
        Encode clear_text using key as multiplication
        :param clear_text:
        :param key:
        :return encoded message:
        """
        return self.__algorithm__(clear_text, key)

    def decode(self, encoded_text, key):
        """
        Decode encoded_text using mod inverse.
        :param encoded_text:
        :param key:
        :return decoded message:
        """
        return self.__algorithm__(encoded_text, key)

    def __algorithm__(self, message, key):
        """
        Encode/Decode message based on key value
        :param message: encoded or clear text
        :param key: key or inverse key
        :return:
        """
        new_message = ""
        for letter in message.upper():
            new_letter = chr((ord(letter) * key) % Cipher.alphabet_length)
            new_message += new_letter
        return new_message

    def generate_keys(self):
        while True:
            key_encrypt = random.randint(0, Cipher.alphabet_length-1)
            if gcd(key_encrypt, Cipher.alphabet_length) == 1:
                break
        key_decrypt = modular_inverse(key_encrypt, Cipher.alphabet_length)
        return key_encrypt, key_decrypt

    def possible_keys(self):
        return Cipher.alphabet_length
