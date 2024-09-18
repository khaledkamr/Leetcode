class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        maxSize = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            maxSize = max(maxSize, right - left)

        return maxSize
