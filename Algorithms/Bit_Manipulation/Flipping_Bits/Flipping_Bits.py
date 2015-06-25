def flipbit(a):
    answer = a^0b11111111111111111111111111111111
    print(answer)

if __name__ == '__main__':
  inputs = []
  num = int(input())
  for i in range(num):
      inputs.append(int(input()))
  for input in inputs:
      flipbit(input)
