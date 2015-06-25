def Kaprekar(a, b):
    answer = []
    for i in range(a, b):
        if i < 10:
            if i == 1 or i ==9:
                answer.append(i)
            continue
        square = str(i*i)
        firsthalf, secondhalf = square[:len(square)//2], square[len(square)//2:]
        thesum = int(firsthalf) + int(secondhalf)
        if thesum == i:
            answer.append(i)
    if len(answer) == 0:
        print('INVALID RANGE')
    else:
        print(*answer)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    Kaprekar(a, b+1)
