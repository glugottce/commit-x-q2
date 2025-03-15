def majorityElement(arr):
    arr.sort()
    n = len(arr)
    count = 1
    result = []
    
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            if count > n // 3:
                result.append(arr[i - 1])
            count = 1 

    if count > n // 3:
        result.append(arr[-1])

    return result if result else [-1]


N = int(input())  
arr = list(map(int, input().split()))  

print(*majorityElement(arr))
