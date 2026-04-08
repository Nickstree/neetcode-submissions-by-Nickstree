class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            ans[i] = prefix
            prefix *= nums[i]
        suffix = 1
        for i in range(len(nums)-2, -1, -1):
            suffix *= nums[i+1]
            ans[i] *= suffix
        return ans