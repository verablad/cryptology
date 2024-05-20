import random
import string


def read_from_file(path):
    with open(path) as file:
        message = file.read()
        return message


def stretch_key(key, message_length):
    key_new = (key * (message_length // len(key) + 1))[:message_length]
    return key_new


class VigenereCipher:
    LETTERS = string.ascii_letters + " " + ".,!?\\\n" + "+-0123456789"
    letter_to_index = {k: v for k, v in zip(LETTERS, range(len(LETTERS)))}
    index_to_letter = {v: k for k, v in letter_to_index.items()}

    def __init__(self, path):
        self.message = read_from_file(path)
        self.key = stretch_key(self.get_key(len(self.message)), len(self.message))
        self.encoded = ""

    def get_key(self, length):
        return "".join(random.choice(VigenereCipher.LETTERS) for _ in range(length))

    def encode(self):
        encoded_message = ""
        for i in range(len(self.message)):
            if self.message[i] in VigenereCipher.letter_to_index:
                number = (VigenereCipher.letter_to_index[self.message[i]] + VigenereCipher.letter_to_index[
                    self.key[i]]) % len(VigenereCipher.LETTERS)
                encoded_message += VigenereCipher.index_to_letter[number]
            else:
                encoded_message += self.message[i]
        self.encoded = encoded_message
        return encoded_message

    def decode(self):
        decoded_message = ""
        for i in range(len(self.encoded)):
            if self.encoded[i] in VigenereCipher.letter_to_index:
                number = (VigenereCipher.letter_to_index[self.encoded[i]] - VigenereCipher.letter_to_index[
                    self.key[i]]) % len(VigenereCipher.LETTERS)
                decoded_message += VigenereCipher.index_to_letter[number]
            else:
                decoded_message += self.encoded[i]
        return decoded_message

    def __str__(self):
        return (f"Message: {self.message}\n\n"
                f"Key: {self.key}\n\n"
                f"Encoded: {self.encoded}\n\n"
                f"Decoded: {self.decode()}\n\n")

