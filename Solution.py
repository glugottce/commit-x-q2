def majorityElementNby3(arr):
    if not arr:
        return -1
    count1, count2, candidate1, candidate2 = 0, 0, None, None
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
    count1, count2 = 0, 0
    for num in arr:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    result = []
    n = len(arr)
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)
    return result if result else -1
arr = list(map(int, input().split()))
print(majorityElementNby3(arr))
