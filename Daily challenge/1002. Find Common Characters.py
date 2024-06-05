class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

        cnt = Counter(words[0])

        for word in words[1:]:
            curr = Counter(word)
            for char in cnt:
                cnt[char] = min(cnt[char], curr[char])
            
        res = []
        for char, count in cnt.items():
            res.extend([char] * count)
        
        return res