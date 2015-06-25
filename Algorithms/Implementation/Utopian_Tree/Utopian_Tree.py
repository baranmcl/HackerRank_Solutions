def utree(a):
    H = 1
    i = 0
    while i < a:
        if i % 2 == 1:
            H = H + 1
            i = i + 1
        else:
            H = H * 2
            i = i + 1
    answer = H
    print(answer)

if __name__ == '__main__':
  inputs = []
  num = int(input())
  for i in range(num):
      inputs.append(int(input()))
  for input in inputs:
      utree(input)
