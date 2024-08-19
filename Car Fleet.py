target=10
position=[6,8]
speed=[3,2]
stack = []
dicts = {}
for i in range(len(position)):
    dicts[position[i]] = (target - position[i]) / speed[i]
print(dicts)
sorted_dict = sorted(dicts.keys(), reverse = True)
print(sorted_dict)
for j in sorted_dict:
    
    print(f'j : {j}')
    if len(stack) == 0:
        stack.append(dicts[j])
    else: 
        if dicts[j] > stack[-1]:
            stack.append(dicts[j])
        else:
            continue
    print(stack)
            
    
print(len(stack))