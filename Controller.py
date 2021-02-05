from Caesar import Caesar
from Multiplication import Multiplication
from Sender import Sender
from Receiver import Receiver
from Hacker import Hacker
from Affine import Affine
from Unbreakable import Unbreakable
from RSA import RSA

cipher_list = {"Caesar": Caesar(), "Multiplication": Multiplication(),
               "Affine": Affine(), "Unbreakable": Unbreakable()}


def main():
    verify_ciphers()
    # verify_hacker()


def verify_hacker():
    for name, cipher in cipher_list.items():

        key_encrypt, key_decrypt = cipher.generate_keys()

        sender = Sender(cipher=cipher, key=key_encrypt)
        receiver = Receiver(cipher=cipher, key=key_decrypt)
        hacker = Hacker(cipher=cipher)

        clear_text = "Hello World"

        encrypted_message = sender.send_message(clear_text)
        decrypted_message = receiver.receive_message(encrypted_message)
        decrypted_hacker = hacker.receive_message(encrypted_message)

        print(" ")
        print(f"Current cipher: {name}")
        print("Clear text: ", clear_text)
        print("Hacked: ", decrypted_hacker)


def verify_ciphers():
    rsa = RSA()
    for i in range(100):
        for cipher_name, ciphers in cipher_list.items():
            if not ciphers.verify("test"):
                print(f"{cipher_name} failed!")
                break
        if not rsa.verify("test"):
            print("RSA failed!")
            break


if __name__ == '__main__':
    main()
