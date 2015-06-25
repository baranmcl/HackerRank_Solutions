def solveMeSecond(a,b):
   return a+b

if __name__ == '__main__':
  n = int(input())
  for i in range(0,n):
      a, b = input().split()
      a,b = int(a),int(b)
      res = solveMeSecond(a,b)
      print(res)
