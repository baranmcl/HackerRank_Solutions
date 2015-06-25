def findposition(x, y):
    return y.index(x)

if __name__ == '__main__':
    V = int(input())
    length = int(input())
    numbers = input()
    numbers = numbers.strip().split(" ")
    numbers = [int(i) for i in numbers]
    print(findposition(V, numbers))
