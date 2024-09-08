# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        res = [None] * k
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        div = size // k
        reminder = size % k
        curr = head
        for i in range(k):
            res[i] = curr
            currSize = div + (1 if reminder > 0 else 0)
            reminder -= 1

            for j in range(currSize - 1):
                if curr:
                    curr = curr.next

            if curr:
                temp = curr.next
                curr.next = None
                curr = temp

        return res
