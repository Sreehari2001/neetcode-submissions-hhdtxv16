class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in x:
                return [x[diff], i]
            x[nums[i]] = i
