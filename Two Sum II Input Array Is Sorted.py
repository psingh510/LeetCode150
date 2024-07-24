numbers = [1, 2, 3, 4, 5, 6]
target = 10
l,r = 0, len(numbers) - 1
while l<r:
    while r>l and r<len(numbers):
        if numbers[l] + numbers[r] == target:
            print([l+1,r+1])
            break
        else:
            r  -= 1
    r = len(numbers) - 1
    l +=1
