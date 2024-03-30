class Solution(object):
    def atMost(self, nums, k):
        freq = {}
        start = count = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
            while len(freq) > k:
                freq[nums[start]] -= 1
                if freq[nums[start]] == 0:
                    del freq[nums[start]]
                start += 1
            count += (i - start + 1)
        return count

    def subarraysWithKDistinct(self, nums, k):
        return self.atMost(nums, k) - self.atMost(nums, k-1)

        