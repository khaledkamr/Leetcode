class Solution:
    def reverse(self, node: ListNode) -> ListNode:
        curr = node
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverse(head)
        curr = head
        prev = None
        carry = 0
        
        while curr:
            value = curr.val * 2 + carry
            curr.val = value % 10
            if value > 9:
                carry = 1
            else:
                carry = 0
            prev = curr
            curr = curr.next
        
        if carry:
            prev.next = ListNode(carry)
        
        return self.reverse(head)
