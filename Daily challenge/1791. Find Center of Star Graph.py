class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        hash_map = {}
        for edge in edges:
            for e in edge:
                hash_map[e] = 1 + hash_map.get(e, 0)

            print(hash_map)
            for n in hash_map:
                if hash_map[n] >= 2:
                    return n
