def findnumber(x):
    x = str(x)
    digits = range(1,10)
    count = 0
    for i in x:
        if (int(i) in digits) and (int(x) % int(i) == 0): 
            count = count +1
    return count

if __name__ == '__main__':
  a = int(input())
  for i in range(a):
      i = int(input())
      print(findnumber(i))
