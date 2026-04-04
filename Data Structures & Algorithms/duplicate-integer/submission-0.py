class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = {}
        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        for i in x:
            if x[i] > 1:
                return True
        return False