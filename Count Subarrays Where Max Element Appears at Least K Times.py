class Solution(object):
    def countSubarrays(self, nums, k):
        
        Max = max(nums)
        start = count = 0

        for i in range(len(nums)):
            if nums[i] == Max:
                k -= 1
            
            while k == 0:
                if nums[start] == Max:
                    k += 1
                start += 1
            
            count += start
        
        return count
        