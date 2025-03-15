from collections import Counter

def find_majority_elements(arr):
    n = len(arr)
    threshold = n // 3 

    freq = Counter(arr)
    
    result = [key for key, value in freq.items() if value > threshold]

    return result if result else [-1]

n = int(input())  
arr = list(map(int, input().split()))  

print(*find_majority_elements(arr))
