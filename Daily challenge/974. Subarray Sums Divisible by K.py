class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefixSum = 0
        prefixCount = {0: 1}

        for n in nums:
            prefixSum += n
            remainder = prefixSum % k

            res += prefixCount.get(remainder, 0)
            prefixCount[remainder] = 1 + prefixCount.get(remainder, 0)

        return res
