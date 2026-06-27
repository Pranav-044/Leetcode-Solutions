# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev=None
        fast=head
        slow=head
        curr=head
        if not head:
            return False
        if(head.next==None):
            return True
        while(fast and fast.next):
            slow=slow.next
            fast=fast.next.next
        temp=slow
        while(slow):
               temp=slow.next
               slow.next=prev
               prev=slow
               slow=temp
        while(prev):
            if(prev.val!=curr.val):
                return False
            prev=prev.next
            curr=curr.next
            
        return True


        
