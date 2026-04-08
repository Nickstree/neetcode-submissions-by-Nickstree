class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ch_dict = defaultdict(int)
        l = 0
        res = 0
        max_f = 0
        for r in range(len(s)):
            ch_dict[s[r]] += 1
            max_f = max(max_f, ch_dict[s[r]])
            while (r - l + 1) - max_f > k:
                ch_dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)

        return res
            
