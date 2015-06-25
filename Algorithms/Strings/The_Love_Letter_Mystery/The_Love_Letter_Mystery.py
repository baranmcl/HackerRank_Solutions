def palindromer(x):
    answer = 0
    f = -1
    g = 0
    poop = []
    for letters in x:
        poop.append(letters)
    while g < len(poop):
        if poop[f] != poop[g]:
            if ord(poop[g]) > ord(poop[f]):
                sub = chr(ord(poop[g])-1)
                poop[g] = sub
                answer = answer + 1
            else:
                sub = chr(ord(poop[f])-1)
                poop[f] = sub
                answer = answer + 1
        else:
            f = f - 1
            g = g + 1
    return answer

if __name__ == '__main__':
  inputs = []
  num = int(input())
  for i in range(num):
      a = str(input())
      inputs.append(a)
  for yep in inputs:
      print(palindromer(yep))
