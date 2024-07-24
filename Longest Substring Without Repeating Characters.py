s = "abcabcbb"
l = 0
r = 1
ls = []
while l < r and r < len(s):
    if l ==0:
        ls.append(s[l])
    print(l)
    print(r)  
    if s[l] != s[r]:
        if s[r] not in ls:
            ls.append(s[r])
            r += 1
            l += 1
            print(ls)
            print(l)
            print(r)
        else:
            if r != len(s):
                ls = []
            
    else:
        l = r
        r = l+1
        if r != len(s):
            ls = []
        print(l)
        print(r)
print(len(ls))