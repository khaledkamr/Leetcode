class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head
        curr = head.next
        front = head.next.next
        indx = 2
        critical = []
        while curr.next:
            if (curr.val < prev.val and curr.val < front.val) or (curr.val > prev.val and curr.val > front.val):
                critical.append(indx)
                
            prev = prev.next
            curr = curr.next
            front = front.next
            indx += 1
        
        if len(critical) < 2:
            return [-1, -1]
        else:
            M = critical[-1] - critical[0]
            m = float("inf")
            for i in range(len(critical) - 1):
                m = min(m, critical[i+1] - critical[i])
            return [m, M]
