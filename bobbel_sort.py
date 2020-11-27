def sort(num):
    for i in range(len(num) -1,0,-1):
        for j in range(i):
            if num[j]>num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]

    return num
nums = [1,23,2,4,0,3,6,5,7,8,9]

sort(nums)
print(nums)