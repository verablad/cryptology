LETTERS = ''.join(chr(i) for i in range(128))
unicode_letters = [ord(i) for i in LETTERS]

dict_letters = {k: v for k, v in zip(LETTERS, unicode_letters)}
reversed_letters = {v: k for k, v in dict_letters.items()}


def stretch_key(key, message):
    key_new = (key * (len(message) // len(key) + 1))[:len(message) + 1]
    return key_new


def encode_Verman(message, key):
    encoded_message = ""
    stretched_key = stretch_key(key, message)
    for i in range(len(message)):
        new_symbol = dict_letters[message[i]] ^ dict_letters[stretched_key[i]]
        encoded_message += reversed_letters[new_symbol]
    return encoded_message


def decode_Verman(encoded_message, key):
    decoded_message = ""
    stret_key = stretch_key(key, encoded_message)
    for i in range(len(encoded_message)):
        new_symbol = dict_letters[encoded_message[i]] ^ dict_letters[stret_key[i]]
        decoded_message += reversed_letters[new_symbol]
    return decoded_message


messag = "Hello World!"
key = ("python")
print(f"Message: {messag}")
print()
print("Encoding: ")
print(encode_Verman(messag, key))
print()
print("Decoding:")
print(decode_Verman(encode_Verman(messag, key), key))
print()
