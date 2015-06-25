def altchar(x):
    answer = 0
    poop = []
    i = 0
    g = 1
    for letter in x:
        poop.append(letter)
    while g < len(poop):
        if poop[i] == poop[g]:
            answer = answer + 1
            g = g + 1
        else:
            i = g
            g = g + 1
    return answer


inputs = []
num = int(input())
for i in range(num):
    a = str(input())
    inputs.append(a)
for yep in inputs:
    print(altchar(yep))
