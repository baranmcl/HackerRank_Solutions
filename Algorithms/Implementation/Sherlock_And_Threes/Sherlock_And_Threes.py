def sherlock(n):
    rem = n % 3
    threes = ((3 -rem) % 3) * 5
    fives = n - threes
    if fives < 0:
        return -1
    else:
        return int("5"*fives + "3"*threes)
    

if __name__ == '__main__':
  a = int(input())
  for i in range(a):
      i = int(input())
      print(sherlock(i))
