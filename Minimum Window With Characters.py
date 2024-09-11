s = "OUZODYXAZV"
t = "XYZ"
lst = [ j for j in t]
l = 0
r = len(s) - 1
while s[l] not in lst:
    l += 1
    
while s[r] not in lst:
    r -= 1
count = len(t)   
for l in range(l,r,1):
    while count != 0:
        output = output + s[l]
        if s[l] in lst:
            count -= 1
            
        


    
        
