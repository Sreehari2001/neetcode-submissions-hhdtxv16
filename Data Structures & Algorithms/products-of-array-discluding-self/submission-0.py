class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        x = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            x[i] = x[i] * prefix
        for i in range(len(nums)-1, 0, -1):
            postfix *= nums[i]
            x[i-1] = x[i-1] * postfix
        return x
        