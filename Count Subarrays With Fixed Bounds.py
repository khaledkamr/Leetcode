class Solution(object):
    def countSubarrays(self, nums, minK, maxK):
        
        count = 0
        left = mini = maxi = -1

        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                left = i
            
            if nums[i] == minK:
                mini = i

            if nums[i] == maxK:
                maxi = i

            count += max(0, min(maxi, mini) - left)
        
        return count
        
        