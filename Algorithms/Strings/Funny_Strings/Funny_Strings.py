def funny(x):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    backwards = x[::-1]
    for i in range(len(x)-1):
        answer = abs(alphabet.index(str(x[i])) - alphabet.index(str(x[i+1])))
        backwards_answer = abs(alphabet.index(str(backwards[i])) - alphabet.index(str(backwards[i+1])))
        if answer != backwards_answer: return 'Not Funny'
    return 'Funny'

if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        string = list(input())
        print(funny(string))
