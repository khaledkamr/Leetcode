class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for s, t in edges:
            graph[s].append(t)
            graph[t].append(s)
        
        output = [0] * n
        count = [1] * n
        self.root = 0

        def DFS(curr, parent, depth):
            o = 1
            for child in graph[curr]:
                if child != parent:
                    o += DFS(child, curr, depth + 1)
                    self.root += (depth + 1)
            count[curr] = o
            return o
        DFS(0, -1, 0)

        def DFS2(curr, parent, ans_p):
            output[curr] = ans_p
            for child in graph[curr]:
                if child != parent:
                    DFS2(child, curr, ans_p + (n - count[child]) - count[child])
        
        DFS2(0, -1, self.root)
        return output