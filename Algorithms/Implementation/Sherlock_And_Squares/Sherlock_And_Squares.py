def findsquares(b):
    min = int(b[0]**0.5)
    max = int(b[1]**0.5)
    answer = max - min
    if min ** 2 == b[0]:
        answer = answer + 1
    return answer


a = int(input())
for i in range(a):
    b = input()
    b = b.strip().split(" ")
    b = [int(i) for i in b]
    print(findsquares(b))
