class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        n = len(nums)
        for i in range(n):
            if nums[i] in x:
                return True
            x[nums[i]] = 1
        return False
        