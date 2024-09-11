class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ["a", "e", "i", "o", "u"]
        count = sum(1 for i in range(k) if s[i] in vowels)
        maxCount = count

        for right in range(k, len(s)):
            if s[right] in vowels:
                count += 1
            if s[right - k] in vowels:
                count -= 1
            maxCount = max(maxCount, count)

        return maxCount
