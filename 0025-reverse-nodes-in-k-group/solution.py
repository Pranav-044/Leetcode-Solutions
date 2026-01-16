class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        for i in range(k):
            if curr is None:
                return head
            curr=curr.next
        c=head
        prev=None
        for i in range(k):
            nxt=c.next
            c.next=prev
            prev=c
            c=nxt
        head.next = self.reverseKGroup(curr,k)

        return prev
