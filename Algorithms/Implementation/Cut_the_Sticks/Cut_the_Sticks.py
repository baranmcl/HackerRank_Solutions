def cutsticks(x):
    stickscutcount = []
    while len(x) > 0:
        x = [i-min(x) for i in x]
        stickscutcount.append(len(x))
        x= [i for i in x if i != 0]
    for i in stickscutcount:
        print(i)


if __name__ == '__main__':
    a = int(input())
    b = input()
    b = b.strip().split()
    b = [int(i) for i in b]
    cutsticks(b)
