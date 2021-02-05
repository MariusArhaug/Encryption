"""Inheritance"""
from Cipher import Cipher
from Multiplication import Multiplication
from Caesar import Caesar


class Affine(Cipher):
    """
    Affine cipher that uses a combination of Caesar and Multiplication cipher
    """

    def __init__(self):
        self.__caesar__ = Caesar()
        self.__multi__ = Multiplication()

    def encode(self, clear_text, key):
        """
        Encode message, first with multiplication then caesar.
        :param clear_text: clear text
        :param key: Tuple, (Multi_key, Caesar_key)
        :return: encoded message
        """
        encoded_multi = self.__multi__.encode(clear_text, key[0])
        encoded_caesar = self.__caesar__.encode(encoded_multi, key[1])
        return encoded_caesar

    def decode(self, encoded_text, key):
        """
        Decode message, first with caesar then multiplication
        :param encoded_text: encoded message
        :param key: Tuple, (Multi_key, Caesar_key)
        :return: decoded message
        """
        decoded_caesar = self.__caesar__.decode(encoded_text, key[1])
        decoded_multi = self.__multi__.decode(decoded_caesar, key[0])
        return decoded_multi

    def generate_keys(self):
        """
        Generates two keys for sender and receiver
        :return: keys with (Multiplication, Caesar) and inverse of that
        """

        key_1_1, key_2_1 = self.__multi__.generate_keys()
        key_1_2, key_2_2 = self.__caesar__.generate_keys()
        return (key_1_1, key_1_2), (key_2_1, key_2_2)

    def possible_keys(self):
        return self.__multi__.possible_keys() * self.__caesar__.possible_keys()