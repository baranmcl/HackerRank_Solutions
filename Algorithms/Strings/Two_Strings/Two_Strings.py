def twostrings(x, y):
    for i in x:
        if i in y: return "YES"
    return "NO"

a = int(input())
for i in range(a):
    b = str(input())
    c = str(input())
    print(twostrings(b, c))
