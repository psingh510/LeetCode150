s = "Was it a car or a cat I saw?"
for i in s:
    if not(i.isalnum()):
        s = s.replace(i, '')
s = s.lower()
print(s)
cnt = 0
for i in range(int(len(s)/2)):
    if s[i] != s[len(s)-i-1]:
        print(False)
        break
    else:
        cnt +=1
print(len(s)/2)

if cnt == int(len(s)/2):
    print(True)
    
# Optimised solution    
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l , r = 0, len(s)-1
        while l < r:
            while l<r and not(s[l].isalnum()):
                l += 1
                
            while l<r and not(s[r].isalnum()):
                r -= 1
                
            if s[l].lower() != s[r].lower():
                return False
            l , r = l + 1 , r-1
        return True
                
            