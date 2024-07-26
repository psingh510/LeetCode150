s1 = "abc"
s2 = "lecaabee"
dict_1 = {}

for i in s1:
    dict_1[i] = 1 + dict_1.get(i,0)
dict_1 = dict(sorted(dict_1.items(),key = lambda x : x[0]))
print(dict_1)
l = 0   
for l in range(len(s2)):
    # r = l
    cnt = 0
    dict_2 = {}
    # print(r)
    for r in range(l,len(s1)+l,1):
        print(r)
        print(s2[r])
        if r >= len(s2):
            break
        else:
            if s2[r] in dict_1.keys():
                dict_2[s2[r]] = 1 + dict_2.get(s2[r],0)
                cnt += 1 
                print(f'Count {cnt}')
                print(r)
            else:
                break
    # l = r + 1
    dict_2 = dict(sorted(dict_2.items(),key = lambda x : x[0]))
    print(dict_2)
    if cnt == len(s1) and dict_2 == dict_1:
        print(True)
        break
    else:
        l = r
        print(f'pointer {l}')
        continue
if cnt != len(s1):   
    print(False)
    
    
# Optimised solution

if len(s1) > len(s2):
    return False


count_s1 = [0] * 26
count_s2 = [0] * 26


for char in s1:
    count_s1[ord(char) - ord('a')] += 1


for char in s2[:len(s1)]:
    count_s2[ord(char) - ord('a')] += 1

for i in range(len(s2) - len(s1)):
    if count_s1 == count_s2:
        return True
    # Add new character to the window
    count_s2[ord(s2[i + len(s1)]) - ord('a')] += 1
    # Remove the character that is sliding out of the window
    count_s2[ord(s2[i]) - ord('a')] -= 1


return count_s1 == count_s2
    
    
    
    


        
        
    