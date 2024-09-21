class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def DFS(curr):
            if curr > n:
                return
            res.append(curr)
            curr *= 10
            for i in range(10):
                DFS(curr + i)

        for i in range(1, 10):
            DFS(i)

        return res
