def ROTnDecoder(letters, shift):
    shift %= 26
    decoded = ""
    for letter in letters:
        if letter.isalpha() and letter.islower():
            stayInAlphabet = ord(letter) + shift
            if stayInAlphabet > ord('z'):
                stayInAlphabet -= 26
            finalletter = chr(stayInAlphabet)
            decoded += finalletter
        elif letter.isalpha() and letter.isupper():
            stayInAlphabet = ord(letter) + shift
            if stayInAlphabet > ord('Z'):
                stayInAlphabet -= 26
            finalletter = chr(stayInAlphabet)
            decoded += finalletter
        else:
            decoded += letter
    return decoded

if __name__ == '__main__':
    b = int(input())
    message = str(input())
    rotation = int(input())
    print(ROTnDecoder(message, rotation))
