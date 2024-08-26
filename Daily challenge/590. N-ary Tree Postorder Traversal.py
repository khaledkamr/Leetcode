"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: "Node") -> List[int]:
        res = []

        def DFS(node):
            if not node:
                return

            for child in node.children:
                DFS(child)
            res.append(node.val)

        DFS(root)
        return res
