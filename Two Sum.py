nums = [4,5,5]
target = 9
r = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        else:
            if nums[i] + nums[j] == target:
                r.append(i)
                r.append(j)

print(r[:2])

