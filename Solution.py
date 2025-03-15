n = int(input())
l = list(map(int, input().split()))

max_elem = []
max_count = n / 3

for i in l:
    if l.count(i) >= max_count:
        max_elem.append(i)
if max_elem:
    print(*list(set(max_elem)))
else:
    print(-1)
