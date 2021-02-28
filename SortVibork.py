nums = [5,7,6,9,8,2,4,3,1]
print('было :', nums)

for i in range(len(nums)):
    lowest = i
    for j in range (i+1,len(nums)):
        if nums[j] < nums[lowest]:
            lowest = j # нашли меньший
    nums[i], nums[lowest] = nums[lowest], nums[i]


print('Стало :', nums)
