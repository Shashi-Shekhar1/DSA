def lenearSearch(list1,a):
    for i in range(len(list1)):
        if list1[i] == a:
            return i
    return -1
list1 = [4,3,1,8,4,2]
a=8
result = lenearSearch(list1,a)
if result == -1:
    print("element not found")
else:
    print(f"element found at index {result}")
