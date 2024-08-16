nums = [3,4,5,6,8,2]
begin = 0
end = len(nums) - 1
minimum = float("inf")
while begin < end:
    midpoint = (begin + end) // 2
    print(f'begin: {begin}')
    print(f'end: {end}')
    print(midpoint)
    minimum = min(minimum,nums[midpoint])

    if nums[midpoint] > nums[end]:
        begin = midpoint + 1

    else:
        end = midpoint -1

print(min(minimum,nums[begin]))
        