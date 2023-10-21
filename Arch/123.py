
def sort(s):
    if len(s) <= 1:
        return (s)
    ref = s[0]
    left = list(filter(lambda x: x < ref, s))
    center = [i for i in s if i == ref]
    right = list(filter(lambda x: x > ref, s))
    return sort(left) + center + sort(right)


print(sort([1,2,5,9,3,6,8,3,5,8,0,2,4,7,3,]))
print(sort([1,2,5,9,3,6,8,3,5,8,0,2,4,7,3,]))

