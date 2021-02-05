"""
Inheritance from Person
"""
from Person import Person


class Sender(Person):
    """
    Subclass of Person, send encoded messages
    """
    def __init__(self, cipher, key, name="Sender"):
        """
        Init
        :param cipher:
        :param key:
        :param name:
        """
        super().__init__(cipher, key, name)

    def operate_cipher(self, text):
        """
        encrypt message based on cipher
        :return encrypted message:
        """
        return self.cipher.encode(text, self.key)

    def send_message(self, message=""):
        """
        Send message based on input and encrypt it before sending it.
        :return encrypted message:
        """
        if message == "":
            clear_text = str(input("Message: "))
        else:
            clear_text = message
        return self.operate_cipher(clear_text)
