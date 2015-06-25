def gemstones(x):
    gemcount = 0
    for letter in stones[0]:
        is_gem = True
        for stone in stones[1:]:
            if letter not in stone:
                is_gem = False
                break
        if is_gem:
            gemcount += 1
    return gemcount

if __name__ == '__main__':
    a = int(input())
    stones = []
    for i in range(a):
        b = str(input())
        stones.append(b)
    stones = [''.join(set(i)) for i in stones]
    print(gemstones(stones))
