class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}

        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1

        y = sorted(x.values())
        z = y[len(y)-k:]

        res = []
        for key, value in x.items():
            if value in z:
                res.append(key)
        return res
        