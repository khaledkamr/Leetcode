# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = head
        curr = prev.next
        while curr:
            newNode = ListNode(math.gcd(prev.val, curr.val))
            prev.next = newNode
            newNode.next = curr
            prev = curr
            curr = prev.next

        return head
