class Solution:
    def atMost(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        start = count = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1

            while len(freq) > k:
                freq[nums[start]] -= 1

                if freq[nums[start]] == 0:
                    del freq[nums[start]]

                start += 1

            count += (i - start + 1)

        return count

    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums, k) - self.atMost(nums, k-1)
        