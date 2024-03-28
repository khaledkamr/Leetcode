class Solution(object):
    def maxSubarrayLength(self, nums, k):
        
        freq = Counter()
        start = -1
        end = 0
        res = 0

        for i in range(len(nums)):
            freq[nums[i]] += 1
            while freq[nums[i]] > k:
                start += 1
                freq[nums[start]] -= 1

            res = max(res, end - start)
            end +=1
            
        return res
        