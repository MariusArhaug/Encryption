"""
Inheritance from Person
"""
from Person import Person


class Receiver(Person):
    """
    Subclass of Person, receive messages and decode
    """
    def __init__(self, cipher, key, name="Receiver"):
        """
        Init
        :param cipher:
        :param key:
        :param name:
        """
        super().__init__(cipher, key, name)

    def operate_cipher(self, text):
        """
        decrypt message based on cipher
        :return:
        """
        return self.cipher.decode(text, self.key)

    def receive_message(self, encoded_text):
        """
        Receive message and send it to decode
        :param encoded_text:
        :return:
        """
        return self.operate_cipher(encoded_text)
