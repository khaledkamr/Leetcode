class Solution(object):
    def trap(self, height):
        left = height[0]
        right = height[-1]
        res = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if left <= right:
                res += left - height[i]
                i += 1
                left = max(left, height[i])
            else:
                res += right - height[j]
                j -= 1
                right = max(right, height[j])
        return res