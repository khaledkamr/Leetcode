class Solution:
    res = 0
    def DFS(self, node):
        if not node:
            return [0, 0]
        
        L_size, L_coins = self.DFS(node.left)
        R_size, R_coins = self.DFS(node.right)

        size = 1 + L_size + R_size
        coins = node.val + L_coins + R_coins
        self.res += abs(size - coins)

        return [size, coins]
        

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.DFS(root)
        return self.res