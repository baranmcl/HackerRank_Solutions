def anagram(x, y):
    delcount = 0
    xletters = {}
    yletters = {}
    for letter in x:
        if letter not in xletters:
            xletters[letter] = 1
        else:
            xletters[letter] +=1
    for letter in y:
        if letter not in yletters:
            yletters[letter] = 1
        else:
            yletters[letter] +=1
    for letter in xletters:
        if letter in yletters:
            delcount = delcount + abs(xletters[letter]-yletters[letter])
        else:
            delcount = delcount + xletters[letter]
    for letter in yletters:
        if letter not in xletters:
            delcount = delcount + yletters[letter]
    return delcount
    

if __name__ == '__main__':
    a = str(input())
    b = str(input())
    print(anagram(a, b))
