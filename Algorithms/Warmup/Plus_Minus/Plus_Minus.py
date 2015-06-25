def plusminus(x, y):
    PosCount = 0
    NegCount = 0
    ZCount = 0
    for i in x:
        if i > 0:
            PosCount += 1
        elif i < 0:
            NegCount += 1
        elif i == 0:
            ZCount += 1
    answer = [PosCount, NegCount, ZCount]
    for i in answer:
        i = i / y
        round(i,3)
        print(i)
    
if __name__ == '__main__':
    num = int(input())
    b = [int(i) for i in input().strip().split()]
    plusminus(b, num)
