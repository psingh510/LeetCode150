class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cnt = {}
        max_len = 0
        l = 0
        for i in range(len(s)):

            cnt[s[i]] = 1 + cnt.get(s[i],0)

            while (i-l+1) - max(cnt.values()) > k:
                cnt[s[l]] -=1
                l += 1
            max_len = max(max_len,i-l+1)

        return max_len
            