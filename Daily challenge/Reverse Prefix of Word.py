class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        rev = word
        for i, c in enumerate(word):
            if c == ch:
                rev = word[:i+1][::-1] + word[i+1:]
                break
        return rev
