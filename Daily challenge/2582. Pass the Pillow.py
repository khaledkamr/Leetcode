class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cycles = time // (n - 1)
        remain = time % (n - 1)
        res = 0
        if cycles % 2 != 0:
            res = n - remain
        else:
            res = remain + 1
        return res
