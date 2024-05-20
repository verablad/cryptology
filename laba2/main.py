from random import shuffle
import string


def generate_key():
    """рандомно генерує ключ для шифрування
    та заміняє відповідно до  букв у алфавіті"""
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    list_of_letters = list(alphabet)
    shuffle(list_of_letters)
    result = "".join(list_of_letters)
    print("Generated key: ")
    print(result)

    return {k: v for k, v in zip(alphabet, result)}


def get_from_file(path):
    """Отримує дані з файлу"""
    with open(path) as file:
        a = file.readlines()
        return a


def write_in_file(path, text):
    """Записує зашифроване повідомлення у файл"""
    with open(path, "w") as file:
        file.writelines(text)


def decode(text: str, key: dict):
    """Розшифровує текст"""
    f = "".join([key.get(c, c) for c in text])
    return f


def encode(text: str, key: dict):
    """Зашифровує текст"""
    key_reversed = {v: k for k, v in key.items()}
    return decode(text, key_reversed)


a = generate_key()
message = get_from_file("text/file.txt")
print()
print("Повідомлення з файлу: ")
print(message)
print()
print("Закодоване повідомлення: ")
secret = encode(decode(message, a), a)
print(secret)
print()
print("Розкодоване повідомлення: ")
alaska = decode(secret, a)
print(alaska)

write_in_file("text/output.txt", secret)


