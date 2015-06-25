def pangram(x):
    count = 0
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in x:
            count = count + 1
    if count == 26:
        return "pangram"
    else:
        return "not pangram"
    
if __name__ == '__main__':
    a = str(input()).lower()
    print(pangram(a))
