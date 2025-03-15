def find_elements(arr):
    n = len(arr)
    if n == 0:
        return -1

    
    candidate1, candidate2 = None, None
    count1, count2 = 0, 0

    
    for num in arr:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
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
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result if result else -1

n = int(input("Enter the size of the array: "))
arr = list(map(int, input("Enter the array elements: ").split()))


result = find_elements(arr)
if result == -1:
    print(result)
else:
    print(" ".join(map(str, result)))
