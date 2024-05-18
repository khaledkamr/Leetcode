class Solution 
{
public:
    int res = 0;

    pair<int , int> DFS(TreeNode* node)
    {
        if(!node)
        {
            return {0, 0};
        }

        pair<int, int> left = DFS(node->left);
        pair<int, int> right = DFS(node->right);

        int size = 1 + left.first + right.first;
        int coins = node->val + left.second + right.second;
        res += abs(size - coins);
        return {size, coins};
    }
    int distributeCoins(TreeNode* root) 
    {
        DFS(root);
        return res;
    }
};