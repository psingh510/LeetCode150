class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s_dict, t_dict = {}, {}
            for i in range(len(s)):
                s_dict[s[i]] = 1 + s_dict.get(s[i],0)
                t_dict[t[i]] = 1 + t_dict.get(t[i],0)
                
            for c in s_dict:
                if s_dict[c] != t_dict.get(c,0):
                    return False