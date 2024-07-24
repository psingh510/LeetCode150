class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        outer_dict = {}
        
        for i in strs:
            sum_t = 0
            for j in i:
                sum_t += ord(j)
            ls = []
            if sum_t in outer_dict:
                outer_dict[sum_t].append(i)
            else:
                ls.append(i)
                outer_dict[sum_t] = ls

   

        r = list(outer_dict.values())
        return r
        

            
      
                        

                


