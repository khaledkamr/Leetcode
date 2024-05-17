class Solution:
    def DFS(self, node, target):
        if node == None:
            return None
        
        node.left = self.DFS(node.left, target)
        node.right = self.DFS(node.right, target)

        if not node.left and not node.right and node.val == target:
            return None
            
        return node

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        return self.DFS(root, target)
