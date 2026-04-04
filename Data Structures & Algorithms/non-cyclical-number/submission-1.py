class Solution:
    def isHappy(self, n: int) -> bool:
        a = set()
        while n not in a:
            a.add(n)
            n = self.sumSquares(n)
            if n == 1:
                return True
        return False

    def sumSquares(self, n: int) -> int:  
        s = 0
        while n > 0:
            r = n % 10
            s += (r**2)
            n = n // 10
        return s        