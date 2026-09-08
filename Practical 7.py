def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == key: return mid
        elif arr[mid] < key: low = mid+1
        else: high = mid-1
    return -1

arr = [1,3,5,7,9,11]
print("Linear search 7:", linear_search(arr, 7))
print("Binary search 9:", binary_search(arr, 9))
