class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ' '.join(reversed(s))
        return res