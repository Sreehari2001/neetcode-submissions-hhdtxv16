class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = (n * (n + 1)) // 2
        arr_sum = sum(nums)
        return total - arr_sum
        