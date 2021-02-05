import random
from Cipher import Cipher


class Caesar(Cipher):
    """
    Caesar cipher, encode message with message value + key value
    """

    def encode(self, clear_text, key):
        """
        Encodes message by adding the ascii value plus the key,
        and returning it to a new character
        :param clear_text:
        :param key:
        :return encoded message:
        """
        return self.__algorithm__(clear_text, key)

    def decode(self, encoded_text, key):
        """
        Decodes the encoded text.
        :param encoded_text:
        :param key:
        :return decoded message:
        """
        return self.__algorithm__(encoded_text, -1*key)

    def __algorithm__(self, message, key):
        """
        Main algorithm for encrypting/decrypting messages
        If key is positive -> encrypt
        If key is negative -> decrypt
        :param message:
        :param key:
        :return encrypted/decrypted message:
        """
        new_message = ""
        for letters in message.upper():
            new_letter = chr((ord(letters) + key) % Cipher.alphabet_length)
            new_message += new_letter
        return new_message

    def generate_keys(self):
        key_encrypt = random.randint(0, 94)
        key_decrypt = key_encrypt
        return key_encrypt, key_decrypt

    def possible_keys(self):
        """
        Number of possible keys which is 95 same as cipher length
        :return:
        """
        return Cipher.alphabet_length
