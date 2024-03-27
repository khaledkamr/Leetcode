class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        Max = max(nums)
        ex = {}

        for i in range(len(nums)):
            ex[nums[i]] = True

        for num in range(1, Max):
            if num not in ex:
                return num
        
        if Max < 0:
            return 1
        else: 
            return Max + 1