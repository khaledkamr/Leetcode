class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = ['a', 'e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']
        left = 0
        right = len(s) - 1
        s = list(s)

        while left < right:

            while s[left] not in vowel and left < right:
                left += 1
            
            while s[right] not in vowel and left < right:
                right -= 1
            
            if left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
        
        return ''.join(s)