"""
Person abstract
"""
from abc import ABC, abstractmethod


class Person(ABC):
    """
    Person is an abstract superclass for sender and receiver
    """
    def __init__(self, cipher, key, name="Person"):
        self.key = key
        self.cipher = cipher
        self.__name__ = name

    @property
    def key(self):
        """
        get key
        :return:
        """
        return self.__key__

    @key.setter
    def key(self, key):
        """
        set key
        :type key: object
        """
        self.__key__ = key

    @abstractmethod
    def operate_cipher(self, text):
        """
        Operate the cipher,
        :return:
        """
    def __str__(self):
        """
        ToString method
        :return:
        """
        return self.__name__
