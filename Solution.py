def find_majority(a):
    n = len(a)
    c1 = c2 = 0
    n1 = n2 = None

    for x in a:
        if x == n1:
            c1 += 1
        elif x == n2:
            c2 += 1
        elif c1 == 0:
            n1, c1 = x, 1
        elif c2 == 0:
            n2, c2 = x, 1
        else:
            c1 -= 1
            c2 -= 1

    c1 = c2 = 0
    for x in a:
        if x == n1:
            c1 += 1
        elif x == n2:
            c2 += 1

    res = []
    if c1 > n // 3:
        res.append(n1)
    if c2 > n // 3:
        res.append(n2)

    print(*res if res else -1)

n = int(input())
a = list(map(int, input().split()))
find_majority(a)
