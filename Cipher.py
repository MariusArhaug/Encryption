"""
Abstract class
"""
from abc import ABC, abstractmethod


class Cipher(ABC):
    """
    Cipher superclass for every cipher, abstract
    """

    alphabet_length = 95

    @abstractmethod
    def encode(self, clear_text, key):
        """
        Encode message
        :param clear_text:
        :param key:
        :return:
        """

    @abstractmethod
    def decode(self, encoded_text, key):
        """
        Decode message
        :param encoded_text:
        :param key:
        :return:
        """

    @abstractmethod
    def generate_keys(self):
        """
        Generate keys
        :return:
        """
    @abstractmethod
    def possible_keys(self):
        """
        Return number of possible keys
        :return: number of possible keys
        """

    def verify(self, clear_text):
        """
        Verify that message encoded and message decoded yields same as input
        :param clear_text:
        :return boolean value, True = means encrypting and decrypting works, false if not:
        """
        key_one, key_two = self.generate_keys()
        encoded_text = self.encode(clear_text, key_one)
        return clear_text.upper() == self.decode(encoded_text, key_two)
