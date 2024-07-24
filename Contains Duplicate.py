class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         result = {}
         if len(nums) == 0:
            return 'false'
         else:
            for i, num in enumerate(nums):
                if num in result.keys():
                    result[num] += 1
                else:
                    result[num] = 1
            
            max_value = max(result.items(), key=lambda x: x[1])
            if max_value[1] > 1:
                return 'true'
            else:
                return 'false'