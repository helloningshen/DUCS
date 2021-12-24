# Ceasar Cipher is a substitutional cipher algorithm.

SHIFT = 3


def get_shifted_word(w):
    return (w + 3) % 26

def get_unshifted_word(w):
    return (w - 3) % 26


def encrypt(text, mapping):
    cipher_text = ''
    for w in text:
        if mapping[w] == -1:
            cipher_text += ' '
        else:
            shifted_num = get_shifted_word(mapping[w])
            ciphered_char = list(mapping.keys())[list(
                mapping.values()).index(shifted_num)]
            cipher_text += ciphered_char

    return cipher_text


def decrypt(mapping, cipher_text):
    plain_text = ''
    for w in cipher_text:
        if mapping[w] == -1:
            plain_text += ' '
        else:
            unshifted_num  = get_unshifted_word(mapping[w])
            plain_char = list(mapping.keys())[list(mapping.values()).index(unshifted_num)]    
            plain_text += plain_char
    return plain_text


def ceasar_cipher(mapping, plain_text):
    cipher_text = encrypt(plain_text, mapping)
    return cipher_text


if __name__ == "__main__":
    character_mapping = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
        " ": -1,

    }
    plain_text = "this is fun"

    cipher = ceasar_cipher(character_mapping, plain_text)
    print(f'PlainText: [{plain_text}] \nCipherText: [{cipher}]')

    plain = decrypt(character_mapping, cipher)
    
    print(f'After Decrypting: {plain}')
