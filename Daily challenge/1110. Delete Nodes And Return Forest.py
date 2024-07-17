# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: List[int]
    ) -> List[TreeNode]:
        to_delete = set(to_delete)
        res_set = set([root])

        def DFS(node):
            if not node:
                return None

            res = node
            if node.val in to_delete:
                res = None
                res_set.discard(node)
                if node.left:
                    res_set.add(node.left)
                if node.right:
                    res_set.add(node.right)
            node.left = DFS(node.left)
            node.right = DFS(node.right)
            return res

        DFS(root)
        return list(res_set)
