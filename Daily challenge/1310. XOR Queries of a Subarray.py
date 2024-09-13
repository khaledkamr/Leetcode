class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr) + 1)

        for i in range(1, len(arr) + 1):
            prefix[i] = prefix[i - 1] ^ arr[i - 1]

        res = []
        for L, R in queries:
            res.append(prefix[R + 1] ^ prefix[L])

        return res
