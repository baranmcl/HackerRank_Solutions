def quicksort(b):
    bigger = []
    smaller = []
    value = []
    value.append(b[0])
    for i in b[1:]:
        if i > b[0]:
            bigger.append(i)
        elif i < b[0]:
            smaller.append(i)
    final = smaller + value + bigger
    print(*final)


if __name__ == '__main__':
    a = int(input())
    b = [int(i) for i in input().strip().split()]
    quicksort(b)
