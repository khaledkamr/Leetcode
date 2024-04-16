/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution 
{
public:
    int sumOfLeftLeaves(TreeNode* root) 
    {
        queue<pair<TreeNode*, bool>> qu;
        qu.push({root, false});
        int sum = 0;

        while(!qu.empty())
        {
            auto [node, left] = qu.front();
            qu.pop();

            if(left && !node->left && !node->right)
            {
                sum += node->val;
            }
            if(node->left)
            {
                qu.push({node->left, true});
            }
            if(node->right)
            {
                qu.push({node->right, false});
            }
        }
        return sum;
    }
};