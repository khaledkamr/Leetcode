class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s = []

        def DFS(node):
            if node == None:
                return s
            DFS(node.left)
            DFS(node.right)
            s.append(node.val)
            return s

        return DFS(root)
