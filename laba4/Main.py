from laba4.Vigenere import VigenereCipher

if __name__ == '__main__':
    cipher = VigenereCipher("file.txt")
    cipher.encode()
    cipher.decode()
    print(cipher)