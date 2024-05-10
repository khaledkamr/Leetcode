class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        minLength = min(len(word1), len(word2))
        for i in range(minLength):
            merge += word1[i] + word2[i]

        merge += word1[minLength:] + word2[minLength:] 

        return merge