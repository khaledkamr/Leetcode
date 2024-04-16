class Solution(object):
    def removeKdigits(self, num, k):
        s = []
        for c in num:
            while k and s and s[-1] > c:
                s.pop()
                k -= 1
            s.append(c)
        
        s = s[:len(s) - k]
        res = "".join(s).lstrip('0')
        return res if res else '0'