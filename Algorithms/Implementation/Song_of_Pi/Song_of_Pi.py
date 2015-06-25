def pisong(string):
    numbers = []
    pi = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 3]
    for word in string:
        numbers.append(len(word))
    for i in range(len(numbers)):
        if numbers[i] != pi[i]: return "It's not a pi song."
    return "It's a pi song."

if __name__ == '__main__':
    num = int(input())
    for i in range(num):
        x = [str(i) for i in input().split()]
        print(pisong(x))
