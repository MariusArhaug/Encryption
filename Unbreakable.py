"""
Inherits from Cipher
"""
import random
from Cipher import Cipher


class Unbreakable(Cipher):
    """
    Unbreakable cipher
    """

    def __init__(self):
        super().__init__()
        with open("english_words.txt", 'r') as text_doc:
            self.word_list = set(word.strip('\n').upper() for word in text_doc)
        self.iterate_index = 0

    def encode(self, clear_text, key_word):
        """
        Encode and decode does the same, but key_word needs to be different
        :param clear_text:
        :param key_word:
        :return:
        """
        return self.__algorithm__(clear_text, key_word)

    def decode(self, encoded_text, key_word):
        """
        Encode and decode does the same, but key_word needs to be different
        :param encoded_text:
        :param key_word:
        :return:
        """
        return self.__algorithm__(encoded_text, key_word)

    def __algorithm__(self, message, key_word):
        """
        Encrypt message based on key_word
        Find values of letter in message and letter in key_word sum and make new char.
        :param message: Encrypted or Decrypted message
        :param key_word: key word or inverse of key word
        :return: encrypted/decrypted message
        """

        new_message = ""
        for index, letter in enumerate(message.upper()):
            numeric_value = ord(letter)
            key_value = ord(key_word[index % len(key_word)-1])
            new_letter = chr((numeric_value + key_value) % Cipher.alphabet_length)
            new_message += new_letter
        return new_message

    def generate_keys(self):
        """
        Find a random word from the english_word.txt file and find inverse to that word
        :return: key_one a randomly selected word, key_two which is the inverse key
        """
        # random_index = random.randint(0, len(self.word_list)-1)

        key_encrypt = random.sample(self.word_list, 1)[0]
        key_decrypt = ""
        for e_i in key_encrypt:
            d_i = (Cipher.alphabet_length - ord(e_i)) % Cipher.alphabet_length
            key_decrypt += chr(d_i)

        return key_encrypt, key_decrypt

    def possible_keys(self):
        return len(self.word_list)
