dict_n = {}
nums = [1,1,2,3,3,4,4,4]
k = 2
for i in nums:
    if i in dict_n:
        dict_n[i] += 1
    else:
        dict_n[i] = 1
        
ls = sorted(dict_n.items(), key = lambda x : x[1],reverse=True)
ls1 = []
for i in range(k):
    ls1.append(ls[i][0])
print(ls1)

    