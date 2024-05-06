class Solution:
    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def removeNodes(self, head):
        head = self.reverse(head)
        curr = head
        temp = curr.next
        while curr.next:
            if temp.val < curr.val:
                curr.next = temp.next
                temp = temp.next
            else:
                curr = curr.next
                temp = curr.next
        return self.reverse(head)
