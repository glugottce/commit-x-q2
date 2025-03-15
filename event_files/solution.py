def find(arr, n):
    cand1, cand2, c1, c2 = None, None, 0, 0
    
    for num in arr:
        if num == cand1:
            c1 += 1
        elif num == cand2:
            c2 += 1
        elif c1 == 0:
            cand1, c1 = num, 1
        elif c2 == 0:
            cand2, c2 = num, 1
        else:
            c1 -= 1
            c2 -= 1
    
    c1=c2 = 0
    for num in arr:
        if num == cand1:
            c1 += 1
        elif num == cand2:
            c2 += 1
    
    re = []
    if c1 > n // 3:
        re.append(cand1)
    if c2 > n // 3:
        re.append(cand2)
    
    return [-1] if not re else re

n = int(input().strip())
arr = list(map(int, input().strip().split()))
re = find(arr, n)
print(" ".join(map(str, re)))