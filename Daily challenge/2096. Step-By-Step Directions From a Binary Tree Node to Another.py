# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(
        self, root: Optional[TreeNode], startValue: int, destValue: int
    ) -> str:
        def DFS(node, path, target):
            if not node:
                return ""
            if node.val == target:
                return path

            path.append("L")
            res = DFS(node.left, path, target)
            if res:
                return res

            path.pop()
            path.append("R")
            res = DFS(node.right, path, target)
            if res:
                return res

            path.pop()
            return ""

        start_path = DFS(root, [], startValue)
        dest_path = DFS(root, [], destValue)
        i = 0
        while i < min(len(start_path), len(dest_path)):
            if start_path[i] != dest_path[i]:
                break
            i += 1
        res = ["U"] * len(start_path[i:]) + dest_path[i:]
        return "".join(res)
