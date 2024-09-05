class Solution:
    def missingRolls(self, rolls: list[int], mean: int, n: int) -> list[int]:
        res = []
        m = len(rolls)
        sum_of_n = (mean * (m + n)) - sum(rolls)
        if sum_of_n < 0 or sum_of_n < n:
            return []

        reminder = sum_of_n % n
        base = sum_of_n // n

        for i in range(n):
            if base + reminder > 6:
                res.append(base + (6 - base))
                reminder -= 6 - base
            elif reminder == 0:
                res.append(base)
            else:
                res.append(base + reminder)
                reminder = 0

        if (sum(rolls) + sum(res)) % (m + n) == 0:
            return res
        else:
            return []
