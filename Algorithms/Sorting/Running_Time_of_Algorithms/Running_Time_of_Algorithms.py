def insert(s):
    shiftcount = 0
    for i in range(1, len(s)):
        val = s[i]
        j = i - 1
        while (j >= 0) and (s[j] > val):
            s[j+1] = s[j]
            j = j - 1
            shiftcount = shiftcount + 1
        s[j+1] = val
    print(shiftcount)
    
if __name__ == '__main__':
    a = int(input())
    b = input()
    b = b.strip().split()
    b = [int(i) for i in b]
    insert(b)
