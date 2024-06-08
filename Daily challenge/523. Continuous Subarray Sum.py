class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: -1}
        prefixSum = 0
        for i, n in enumerate(nums):
            prefixSum += n
            reminder = prefixSum % k
            if reminder not in hash_map:
                hash_map[reminder] = i
            elif i - hash_map[reminder] > 1:
                return True
        return False
