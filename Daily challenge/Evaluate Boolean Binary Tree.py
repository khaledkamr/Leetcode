class Solution:
    def DFS(self, node):
        if node.val == 0:
            return False
        elif node.val == 1:
            return True
        elif node.val == 2:
            return self.DFS(node.left) or self.DFS(node.right)
        elif node.val == 3:
            return self.DFS(node.left) and self.DFS(node.right)
        return False

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.DFS(root)
        
        