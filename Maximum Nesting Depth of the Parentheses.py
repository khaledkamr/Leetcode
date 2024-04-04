class Solution(object):
    def maxDepth(self, s):
        curr = 0
        Max = 0
        for char in s:
            if char == '(':
                curr += 1
                Max = max(Max, curr)
            elif char == ')':
                if curr > 0:
                    curr -= 1
                else:  return -1
        if curr != 0:
            return -1
        return Max