def bigsum(n):
    return sum(n)

if __name__ == '__main__':
    num = int(input())
    numbers = [int(i) for i in input().strip().split()]
    print(bigsum(numbers))
