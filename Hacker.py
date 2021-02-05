"""Gather all brute-force crackable ciphers"""
from Receiver import Receiver
from Unbreakable import Unbreakable
from Cipher import Cipher


class Hacker(Receiver):
    """
    Loop through words in txt file and use it as key.
    Check what sentence has the most correct words in nit, brute force
    """

    def __init__(self, cipher=None, name="Hacker"):
        """
        Init receiver constructor
        :param name:
        """
        super().__init__(cipher, None, name)
        # Save all words from text doc in a list, where every word is CAPS
        with open("english_words.txt", 'r') as text_doc:
            self.word_list = set(word.strip('\n').upper() for word in text_doc)

    def operate_cipher(self, text):
        """
        Bruteforce method of finding right clear_text
        Cycle through each individual cipher method,
        see which one has the most number of english words.
        Per Cipher we need to cycle through all the number of key possibilities
        :param text:
        :return:
        """
        # Various messages that has been decrypted [sentence] : number of english words
        decrypted_messages = {}
        _words = iter(self.word_list)
        for i in range(self.cipher.possible_keys()):
            # print(self.cipher.possible_keys())
            if isinstance(self.cipher, Unbreakable):
                key_encrypt = next(_words)
                key_decrypt = ""
                for e_i in key_encrypt:
                    d_i = (Cipher.alphabet_length - ord(e_i)) % Cipher.alphabet_length
                    key_decrypt += chr(d_i)
            else:
                key_encrypt, key_decrypt = self.cipher.generate_keys()

            # Find decoded text
            decoded_text = self.cipher.decode(text.upper(), key_decrypt)

            # Count number of english words in the decoded text
            # and save the text as key and count as value
            count = 0
            for words in decoded_text.split(" "):
                if words in self.word_list:
                    count += 1

            if decoded_text not in decrypted_messages:
                decrypted_messages[decoded_text] = count

        return max(decrypted_messages, key=decrypted_messages.get)
