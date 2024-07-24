result = ""
strs = ["neet","code","love","you"]
for i in strs:
    result = result + i + " "
    
print(result)

ls = []
s = result
s1 = ""
for i in s:
    if i != " ":
        s1 += i
        
        
    else:
        ls.append(s1)
        i = 0
        s = s[len(s1):len(s)]
        s1 = ""
        
print(ls)
    