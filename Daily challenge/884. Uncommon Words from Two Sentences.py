class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s = s1.split(" ") + s2.split(" ")
        freq = defaultdict(int)
        res = []
        for word in s:
            freq[word] += 1

        for word in freq:
            if freq[word] == 1:
                res.append(word)

        return res
