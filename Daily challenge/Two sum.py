class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
       
        for i, n in enumerate(nums, 0):
            x = target - n
            if x in dic:
                return [dic[x], i]
            else: dic[n] = i
        
        return None
        