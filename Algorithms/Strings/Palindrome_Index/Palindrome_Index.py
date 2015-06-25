def palindromeindex(x):
    backwards = x[::-1]
    indexes = []
    if backwards == x: return -1
    for i in range(len(x)):
        if x[i] != backwards[i]:
            indexes.append(i)
    del x[indexes[0]]
    if x == x[::-1]: return indexes[0]
    forwards = backwards[::-1]
    del forwards[max(indexes)]
    if forwards == forwards[::-1]: return max(indexes)


if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        b = [str(i) for i in input()]
        print(palindromeindex(b))
