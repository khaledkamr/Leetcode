class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        hash_table = Counter(arr)
        distinct = []
        for string in hash_table:
            if hash_table[string] == 1:
                distinct.append(string)

        if k > len(distinct):
            return ""
        else:
            return distinct[k - 1]
