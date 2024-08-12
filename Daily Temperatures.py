# temperatures = [34,80,80,80,34,80,80,80,34,34]
temperatures = [30,38,30,36,35,40,28]
result = []
i = 0
for i in range(len(temperatures)):
    count = 0
    for j in range(i+1,len(temperatures),1):
        if j == len(temperatures)-1 and temperatures[j] <= temperatures[i]:
            count = 0
            break
        elif temperatures[i] < temperatures[j]:
            count += 1
            break
        else:
            count += 1
    result.append(count) 

print(result)

# Optimized Solution using Stacks
stack = []
res = [0] * len(temperatures)
for i in range(len(temperatures)-1,-1,-1):
    print(stack)
    while len(stack) != 0 and temperatures[i] >= temperatures[stack[-1]]:
        stack.pop()
    if len(stack) == 0:
        res[i] = 0
    else:
        res[i] = stack[-1] - i
    stack.append(i)
            
print(res)
            

        
        
    