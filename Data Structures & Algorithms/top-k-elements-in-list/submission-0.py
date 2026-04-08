class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, val in count.items():
            freq[val].append(key)
        for i in range(len(freq) - 1, 0, -1):
            res += freq[i]
            if len(res) >= k:
                return res