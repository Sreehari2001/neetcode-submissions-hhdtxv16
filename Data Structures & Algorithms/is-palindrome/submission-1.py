class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = s.lower()
        alpha = 'abcdefghijklmnopqrstuvwxyz0123456789'
        z = []

        for i in x:
            if i in alpha:
                z.append(i)
        return z[::-1] == z
        