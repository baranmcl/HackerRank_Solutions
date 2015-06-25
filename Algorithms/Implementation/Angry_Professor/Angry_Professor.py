def AngryProf(x, y):
    early = 0
    for i in y:
        if i <= 0:
            early = early + 1
    if early >= x[1]:
        return "NO"
    else:
        return "YES"

a = int(input())
for i in range(a):
    b = input()
    b = b.strip().split(" ")
    b = [int(i) for i in b]
    c = input()
    c = c.strip().split(" ")
    c = [int(i) for i in c]
    print(AngryProf(b, c))
