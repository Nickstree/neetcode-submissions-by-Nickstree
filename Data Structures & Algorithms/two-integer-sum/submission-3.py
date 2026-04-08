class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_idx_dict = {}
        for i, num in enumerate(nums):
            j_val = target - num
            if j_val in val_idx_dict:
                return [val_idx_dict[j_val], i]
            val_idx_dict[num] = i