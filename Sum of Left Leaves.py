# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        qu = Queue()
        qu.put((root, False))
        sum = 0

        while not qu.empty():
            node, left = qu.get()

            if left and not node.left and not node.right:
                sum += node.val
            if node.left:
                qu.put((node.left, True))
            if node.right:
                qu.put((node.right, False))
                
        return sum