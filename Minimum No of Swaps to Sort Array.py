arr = [1,0,0,1,0,0,1]
pos_dict = {}
for i in range(len(arr)):
    pos_dict[i] = arr[i]
    
sorted_dict = dict(sorted(pos_dict.items(), key = lambda x : x[1]))
# sorted_dict_1 = dict(sorted(pos_dict.items(), key = lambda x : x[1], reverse = True))
ls = list(sorted_dict.keys())
# ls1 = list(sorted_dict_1.keys())
print(ls)
# print(ls1)
swap1 = 0
for i in range(len(arr)):
    if i == ls[i]:
        continue
    else:
        temp = ls[i] 
        # Perform the swap
        ls[i] = ls[ls[i]]
        ls[temp] = temp
        swap1 += 1
        
# swap = 0
# for i in range(len(arr)):
#     if i == ls1[i]:
#         continue
#     else:
#         temp = ls1[i] 
#         # Perform the swap
#         ls1[i] = ls1[ls1[i]]
#         ls1[temp] = temp
#         swap += 1
print(swap1)

    