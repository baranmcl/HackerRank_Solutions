def diagsum(x, y):
    LtRSum = 0
    RtLSum = 0
    for i in range(x):
        LtRSum += y[i][i]
    for i in range(x):
        RtLSum += y[i][x-i-1]
    return abs(LtRSum - RtLSum)

if __name__ == '__main__':
    num = int(input())
    lines = []
    for i in range(num):
        b = [int(i) for i in input().strip().split()]
        lines.append(b)
    print(diagsum(num, lines))
