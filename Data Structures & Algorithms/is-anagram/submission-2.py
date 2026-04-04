class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = {}
        for i in s:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        for i in t:
            if i in x:
                x[i] -= 1
            else:
                x[i] = 1
        for i in x:
            if x[i] >= 1:
                return False
        return True
        