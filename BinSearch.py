nums = [5,7,6,9,8,2,4,3,1]
print('было :', nums)
nums.sort()
print('Стало :', nums)

search_for = 3
lowest = 0
highest = len(nums)

print(lowest)
print(highest)

index = None # Будущий индекс искомого элемента

while(lowest<= highest) and (index is None):
    # повторяем пока не найдено
    mid = (lowest+highest) // 2 # середина
    if nums[mid] == search_for:
        # нашли по средине
        index=mid
    else:
        if search_for < nums[mid]:
            # ищем в левой части
            highest = mid-1
        else:
            lowest = mid+1
print('Искомый элемент', search_for, 'Находится под индексом', index)
