class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxlen = 0
        for i in nums:
            c = 0
            if (i-1) not in nums:
                while i+c in nums:
                    c+=1
                maxlen = max(c, maxlen)
        return maxlen
