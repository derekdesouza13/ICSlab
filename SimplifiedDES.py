# Simplified DES (S-DES)

# Initial Permutation (IP)
IP = [2, 6, 3, 1, 4, 8, 5, 7]

# Inverse Initial Permutation
IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]

# Expansion Permutation
EP = [4, 1, 2, 3, 2, 3, 4, 1]

# P4 Permutation
P4 = [2, 4, 3, 1]

# S-Boxes
S0 = [
    [1, 0, 3, 2],
    [3, 2, 1, 0],
    [0, 2, 1, 3],
    [3, 1, 3, 2]
]

S1 = [
    [0, 1, 2, 3],
    [2, 0, 1, 3],
    [3, 0, 1, 0],
    [2, 1, 0, 3]
]


def permute(bits, table):
    return ''.join(bits[i - 1] for i in table)


def xor(a, b):
    return ''.join('0' if x == y else '1' for x, y in zip(a, b))


def sbox_lookup(bits, sbox):
    row = int(bits[0] + bits[3], 2)
    col = int(bits[1] + bits[2], 2)
    return format(sbox[row][col], '02b')


def fk(bits, key):
    left = bits[:4]
    right = bits[4:]

    expanded = permute(right, EP)

    xored = xor(expanded, key)

    left_half = xored[:4]
    right_half = xored[4:]

    s0 = sbox_lookup(left_half, S0)
    s1 = sbox_lookup(right_half, S1)

    p4 = permute(s0 + s1, P4)

    left = xor(left, p4)

    return left + right


def swap(bits):
    return bits[4:] + bits[:4]


# Example keys (normally generated from a 10-bit master key)
K1 = "10100100"
K2 = "01000011"

plaintext = input("Enter 8-bit binary plaintext: ")

# Encryption
step1 = permute(plaintext, IP)
step2 = fk(step1, K1)
step3 = swap(step2)
step4 = fk(step3, K2)
cipher = permute(step4, IP_INV)

print("Encrypted Ciphertext:", cipher)