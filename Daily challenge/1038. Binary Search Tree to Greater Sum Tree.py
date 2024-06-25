class Solution:
    def __init__(self):
        self.currSum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            temp = node.val
            node.val += self.currSum
            self.currSum += temp
            dfs(node.left)

        dfs(root)
        return root
