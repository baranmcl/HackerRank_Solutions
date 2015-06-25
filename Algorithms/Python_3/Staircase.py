def staircase(n):
    i = n - 1
    while i >= 0:
        print((" ")*(i) + "#"*(n-i))
        i = i - 1

if __name__ == '__main__':
    num = int(input())
    staircase(num)
