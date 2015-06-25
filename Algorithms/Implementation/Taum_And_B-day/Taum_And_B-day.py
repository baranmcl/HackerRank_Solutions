def giftcost(x, y):
    NoSubsCost = x[0]*y[0] + x[1]*y[1]
    if y[2] == y[0] and y[2] == y[1]:
        return NoSubsCost
    elif y[1] < y[0]:
        SubCost = (x[0] + x[1])*y[1] + (x[0]*y[2])
        if SubCost < NoSubsCost:
            return SubCost
        else:
            return NoSubsCost
    elif y[0] < y[1]:
        SubCost = (x[0] + x[1])*y[0] + (x[1]*y[2])
        if SubCost < NoSubsCost:
            return SubCost
        else:
            return NoSubsCost
    else:
        return NoSubsCost

if __name__ == '__main__':
    a = int(input())
    for i in range(a):
        b = input()
        b = b.strip().split(" ")
        b = [int(x) for x in b]
        c = input()
        c = c.strip().split(" ")
        c = [int(x) for x in c]
        print(giftcost(b, c))
