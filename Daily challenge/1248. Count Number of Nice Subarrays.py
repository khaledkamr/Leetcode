class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        oddCount = 0
        start, mid = 0, 0
        nice = 0
        for end in range(len(nums)):
            if nums[end] % 2 == 1:
                oddCount += 1

            while oddCount > k:
                if nums[start] % 2 == 1:
                    oddCount -= 1
                start += 1
                mid = start

            if oddCount == k:
                while nums[mid] % 2 == 0:
                    mid += 1
                nice += (mid - start) + 1

        return nice
