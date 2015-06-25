def counter(x):
    values = {}
    countinit = [int(i) for i in range(0,100)]
    finalcount = []
    for i in countinit:
        values[i] = 0
    for i in x:
        if i in values:
            values[i] = values[i] + 1
    for i in values:
        value = values[i]
        finalcount.append(value)
    print(*finalcount)


if __name__ == '__main__':
    a = int(input())
    b = [int(i) for i in input().strip().split()]
    counter(b)
