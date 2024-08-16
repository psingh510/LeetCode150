target = 4
nums = [1,2,3,4,5,6]
begin = 0
end = len(nums) - 1
while begin < end:
    
    mid = (begin+end) // 2
    print(mid)
    if target == nums[mid]:
        print(mid)
    if nums[mid] >= nums[begin]:
        if target > nums[mid] or target < nums[begin]:
            begin = mid + 1
        else:
            end = mid - 1   
    else:
        if target < nums[mid] or target > nums[end]:
            end = mid - 1
        else:
            begin = mid + 1
                
