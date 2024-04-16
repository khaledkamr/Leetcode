
class Solution(object):
    def makeGood(self, s):
        res = ""
        for letter in s:
            if res != "" and abs(ord(letter) - ord(res[-1])) == 32:
                res = res[:-1]
            else:
                res += letter
        
        return res
        