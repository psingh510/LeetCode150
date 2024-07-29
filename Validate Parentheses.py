class Solution:
    def isValid(self, s: str) -> bool:
        ls = []
        for i in s:
            if i in ['{' , '[','(']:
                ls.append(i)

            else:
                if len(ls) == 0:
                    return False
                else:
                    p = ls.pop()
                    if i == '}' and p == '{':
                        continue
                    elif i == ')' and p == '(':
                        continue
                    elif i == ']' and p == '[':
                        continue
                    else:
                        return False
        if len(ls) == 0:
            return True
        else:
            return False
            

            

        