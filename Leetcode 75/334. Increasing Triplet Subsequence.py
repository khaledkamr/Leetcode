class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        n1, n2 = float("inf"), float("inf")

        for n in nums:
            if n > n2:
                return True

            if n <= n1:
                n1 = n
            elif n <= n2:
                n2 = n

        return False
