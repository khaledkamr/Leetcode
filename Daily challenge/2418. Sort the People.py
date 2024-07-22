class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        hash_table = {}
        for i in range(len(heights)):
            hash_table[heights[i]] = names[i]
        heights.sort(reverse=True)
        res = []
        for h in heights:
            res.append(hash_table[h])
            
        return res