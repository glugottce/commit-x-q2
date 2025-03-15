from collections import Counter

n = int(input())
arr = list(map(int, input().split()))
f = Counter(arr)

result = [num for num, count in f.items() if count > n // 3]

print(*result if result else -1)
