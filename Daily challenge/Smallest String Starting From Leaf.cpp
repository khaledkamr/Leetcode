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
    string smallestFromLeaf(TreeNode* root) 
    {
        string smallest;
        DFS(root, "", smallest);
        return smallest;
    }

    void DFS(TreeNode* node, string path, string& smallest)
    {
        if(!node)
        {
            return;
        }
        path += char('a' + node->val);
        if(!node->left && !node->right)
        {
            reverse(path.begin(), path.end());
            if(smallest.empty() || path < smallest)
            {
                smallest = path;
            }
            reverse(path.begin(), path.end());
        }
        DFS(node->left, path, smallest);
        DFS(node->right, path, smallest);
    }
};