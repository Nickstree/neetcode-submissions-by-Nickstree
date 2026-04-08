class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_dict = {}
        for num in nums:
            check_dict[num] = check_dict.get(num, 0) + 1
            if check_dict[num] > 1:
                return True
        return False
