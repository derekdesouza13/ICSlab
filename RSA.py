import math


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None


def generate_keys():
    print("Enter two prime numbers")

    p = int(input("Enter p: "))
    q = int(input("Enter q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def encrypt(message, public_key):
    e, n = public_key
    cipher = []

    for ch in message:
        cipher.append(pow(ord(ch), e, n))

    return cipher


def decrypt(cipher, private_key):
    d, n = private_key
    message = ""

    for value in cipher:
        message += chr(pow(value, d, n))

    return message


def main():

    print("========== RSA Algorithm ==========\n")

    public_key, private_key = generate_keys()

    print("\nPublic Key :", public_key)
    print("Private Key:", private_key)

    message = input("\nEnter Message: ")

    cipher = encrypt(message, public_key)

    print("\nEncrypted Message:")
    print(cipher)

    decrypted = decrypt(cipher, private_key)

    print("\nDecrypted Message:")
    print(decrypted)


if __name__ == "__main__":
    main()