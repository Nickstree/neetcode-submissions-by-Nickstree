class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, m = 0, len(nums) - 1, 0
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        min_id = m
        l, r = 0, len(nums) - 1
        if target >= nums[min_id] and target <= nums[r]:
            l = min_id
        elif target >= nums[l] and target <= nums[min_id - 1]:
            r = min_id - 1
        else:
            return -1
        
        while l <= r:
            m = l + (r - l) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1