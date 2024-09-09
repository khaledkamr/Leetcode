class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kid_with_greatest = max(candies)
        res = [False] * len(candies)
        for i in range(len(candies)):
            if candies[i] + extraCandies >= kid_with_greatest:
                res[i] = True
        return res