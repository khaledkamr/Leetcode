# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head.next
        temp = dummy
        sum = 0
        while curr:
            sum += curr.val
            if curr.val == 0:
                node = ListNode(sum)
                sum = 0
                temp.next = node
                temp = temp.next
            curr = curr.next

        return dummy.next
