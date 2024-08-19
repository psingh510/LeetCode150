s = "OUZODYXAZV"
t = "XYZ"
lst = [ j for j in t]
print(lst)
output = ''
final = []
count = len(lst)
for i in s:
    print(f'char {i}')
    print(count)
    if i in lst:
        output = output + i
        count -= 1
        if count  == 0:
            final.append(output)
            output = ''
            count = len(lst)
    elif count < len(lst):
        output = output + i
        
print(output)