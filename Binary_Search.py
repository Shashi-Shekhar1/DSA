ef binarySearch(list1,a):
    left = 0
    right = len(list1) - 1
    while left <=  right:
        mid = (left + right) // 2
        if list1[mid] == a:
            return mid
        elif list1[mid] < a:
            left = mid + 1
        else:
            right = mid - 1
    return -1
list1 = [1,2,4,6,7,9]
a = 6
result = binarySearch(list1,a)
if result == -1:
    print("element not found")
else:
    print(f"element found at {result}")
