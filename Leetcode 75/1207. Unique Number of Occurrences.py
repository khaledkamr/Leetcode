class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        freq = Counter(arr)
        occ = list(freq.values())
        unique = list(set(occ))
        return len(occ) == len(unique)
