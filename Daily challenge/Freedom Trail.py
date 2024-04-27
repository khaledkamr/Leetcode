class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        cache = {}
        def DFS(r, k):
            if k == len(key):
                return 0

            if (r, k) in cache:
                return cache[(r, k)]
            
            res = float('inf')
            for i, c in enumerate(ring):
                if c == key[k]:
                    dist = min(abs(r - i), len(ring) - abs(r - i))
                    res = min(res, dist + 1 + DFS(i, k + 1))
            
            cache[(r, k)] = res
            return res
        return DFS(0, 0)
