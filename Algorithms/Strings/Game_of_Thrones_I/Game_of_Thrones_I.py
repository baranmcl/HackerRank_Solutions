def palindromecheck(x):
    poop = []
    yep = []
    oddcount = 0
    for letters in x:
        poop.append(letters)
    for letter in poop:
        if letter not in yep:
            yep.append(letter)
    for letter in yep:
        if poop.count(letter) % 2 == 1:
            oddcount = oddcount + 1
    if oddcount <= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    a = str(input())
    print(palindromecheck(a))
