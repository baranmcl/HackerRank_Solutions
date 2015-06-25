def maxsubarray(x):
    maxendinghere = maxsofar = x[0]
    for i in x[1:]:
        maxendinghere = max(i, maxendinghere + i)
        maxsofar = max(maxsofar, maxendinghere)
    if max(x) < 0:
        maxsum = max(x)
    else:
        x = [i for i in x if i > 0]
        maxsum = sum(x)
    return ("%s %s" %(maxsofar, maxsum))


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        a = int(input())
        b = [int(i) for i in input().strip().split()]
        print(maxsubarray(b))
