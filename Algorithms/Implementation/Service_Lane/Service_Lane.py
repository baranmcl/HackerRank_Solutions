def servicelane(x, y):
    slice = x[y[0]:y[1]+1]
    return min(slice)

if __name__ == '__main__':
    a = input()
    a = a.strip().split()
    a = [int(i) for i in a]
    b = input()
    b = b.strip().split()
    b = [int(i) for i in b]
    for i in range(a[1]):
        c = input()
        c = c.strip().split()
        c = [int(i) for i in c]
        print(servicelane(b, c))
