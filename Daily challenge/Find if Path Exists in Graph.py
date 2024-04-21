class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n == 1: return True
        vi = [False]*n
        vi[source] = True
        flag = True
        while flag:
            flag = False
            for edge in edges:
                if vi[edge[0]] != vi[edge[1]]:
                    vi[edge[0]] = True
                    vi[edge[1]] = True
                    flag = True
                
                if vi[destination]: return True
        
        return False