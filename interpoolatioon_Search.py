def interpolationSearch(list1,a):
    left = 0
    right = len(list1)-1
    while left <=  right:
        probe = left + (((right-left)*(a-list1[left]))//(list1[right]-list1[left]))
        if list1[probe] == a:
            return probe
        elif a > list1[probe]:
            left = probe + 1
        else:
            right = probe - 1
    return -1
list1 = [2,4,5,6,8,9]
a = 5
result = interpolationSearch(list1,a)
if result == -1:
    print("element not found")
else:
    print(f"element foudn at index {result}")
