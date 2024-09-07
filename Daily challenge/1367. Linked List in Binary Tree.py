# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        return self.dfs(head, head, root)

    def dfs(self, head, cur, root) -> bool:
        if cur is None:
            return True
        if root is None:
            return False

        if cur.val == root.val:
            cur = cur.next
        elif head.val == root.val:
            head = head.next
        else:
            cur = head

        return self.dfs(head, cur, root.left) or self.dfs(head, cur, root.right)
