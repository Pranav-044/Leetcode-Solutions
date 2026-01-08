# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=-1
        length=0
        prev=None
        while curr:
            length+=1
            curr=curr.next
        target=length-n
        curr=head
        if(target==0):
            return head.next
        while curr:
            count+=1
            if(count==target):
                if(curr.next):
                    prev.next=curr.next
                else:
                    prev.next=None
                break
            prev=curr
            curr=curr.next
        return head
        

