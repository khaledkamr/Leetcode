class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        Sum = sum(nums[:k])
        Max = sum(nums[:k])
        for i in range(k, len(nums)):
            Sum += nums[i] - nums[i - k]
            Max = max(Max, Sum)

        return Max / k
