class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = {}
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        for i in x:
            if x[i] > len(nums) // 2:
                return i
        