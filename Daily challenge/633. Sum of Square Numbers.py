class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while left <= right:
            res = left**2 + right**2

            if res < c:
                left += 1
            elif res > c:
                right -= 1
            else:
                return True

        return False
