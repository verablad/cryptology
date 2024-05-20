from sympy import randprime


def extended_euclid(p, q):
    if p == 0:
        return q, 0, 1
    g, y, x = extended_euclid(q % p, p)
    return g, x - (q // p) * y, y


def modular_inverse(e, r):
    g, x, y = extended_euclid(e, r)
    if g != 1:
        exit()
    return x % r
def random_prime():
    return randprime(0, 1000)

def euler_function(p, q):
    return (p - 1) * (q - 1)


def encrypt(secret_message, p, q):
    n = p * q
    e = 65537
    encrypted = ""
    for i in secret_message:
        char_number = ord(i)
        new_char_number = pow(char_number, e, n)
        encrypted += f"{chr(new_char_number)} "

    return encrypted


def decrypt(encrypted_message: str, p, q):
    n = p * q
    e = 65537
    r = euler_function(p, q)
    d = modular_inverse(e, r)
    encrypted_symbols = encrypted_message.strip().split(" ")
    decrypted = ""
    for encrypted_symbol in encrypted_symbols:
        encrypted_value = int(ord(encrypted_symbol))
        decrypted_value = pow(encrypted_value, d, n)
        decrypted_symbol = chr(decrypted_value)
        decrypted += decrypted_symbol
    return decrypted

p = randprime(0, 100)
q = randprime(0, 100)
print("Starter message:")
message = "The secretest secret in the world!"
print(message)
print()
print("Encrypted message: ")
encrypted_message = encrypt(message,p,q)
print(encrypted_message)
print()
print("Decrypted message")
decrypted_message = decrypt(encrypted_message,p,q)
print(decrypted_message)
