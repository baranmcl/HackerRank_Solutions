def anagram(x):
    if len(x) % 2 == 1: return -1
    a = x[:len(x)//2]
    b = x[len(x)//2:]
    Alettercount = {}
    Blettercount = {}
    for letter in a:
        if letter not in Alettercount:
            Alettercount[letter] = 1
        else:
            Alettercount[letter] +=1
    for letter in b:
        if letter not in Blettercount:
            Blettercount[letter] = 1
        else:
            Blettercount[letter] += 1
    for letter in Alettercount:
        if letter in Blettercount:
            Alettercount[letter] = abs(Alettercount[letter] - Blettercount[letter])
    for letter in Blettercount:
        if letter not in Alettercount:
            Alettercount[letter] = Blettercount[letter]
    valuesum = sum(Alettercount.values())
    if valuesum == 0:
        return 0
    else:
        return int(valuesum / 2)

if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        a = list(input())
        print(anagram(a))
