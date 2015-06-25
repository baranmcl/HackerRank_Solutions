#!/usr/bin/py
# Head ends here
def lonelyinteger(b):
    answer = 0
    for i in b:
        answer = answer ^ i
    return answer

# Tail starts here
if __name__ == '__main__':
    a = int(input())
    b = input()
    b = b.strip().split(" ")
    b = [int(i) for i in b]
    print(lonelyinteger(b))
