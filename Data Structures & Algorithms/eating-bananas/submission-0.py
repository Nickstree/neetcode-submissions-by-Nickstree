import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = l + (r - l) // 2
            res = sum([math.ceil(pile / m) for pile in piles])
            # print(l, m, r, res)
            if res > h:
                l = m + 1
            else:
                k = m
                r = m - 1
        return k
            
            