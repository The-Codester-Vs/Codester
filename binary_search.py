place  = -1
list = [12, 23, 34, 45, 46, 48, 50]
# binary search
def binary_search(list,n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u) // 2
        if list[mid] == n:
            globals()['place'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False
n = int(input("Enter the number: "))
if binary_search(list,n):
    print(f"Your number {n} is the list at position {place + 1}")
else:
    print("Your number is not in the list")