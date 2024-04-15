# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def DFS(node, sum):
            if not node: return 0
            sum = sum * 10 + node.val
            if not node.left and not node.right:
                return sum
            return DFS(node.left, sum) + DFS(node.right, sum)
        
        return DFS(root, 0) 