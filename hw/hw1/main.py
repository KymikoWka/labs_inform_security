def read_file():
    content = ''
    with open('./1.txt', 'r', encoding='utf8') as f:
        content = ''.join([line for line in f])
    return content


def encrypt_text(content, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for letter in content.lower():
        if letter in alphabet:
            position = alphabet.index(letter)
            newPosition = (position + key) % len(alphabet)
            encrypted = encrypted + alphabet[newPosition]
        else:
            encrypted += letter
    return encrypted


def write_file(encrypted):
    with open('./2.txt', 'w', encoding='utf8') as f:
        f.write(encrypted)


content = read_file()
text = encrypt_text(content, 3)
write_file(text)
