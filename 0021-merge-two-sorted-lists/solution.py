# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        temp1=list1
        temp2=list2
        final_head=None
        head=None
        if(temp1.val<=temp2.val):
            head=temp1
            final_head=temp1
            temp1=temp1.next
        else:
            head=temp2
            final_head=temp2
            temp2=temp2.next
        while temp1 and temp2 :
            if(temp1.val<=temp2.val):
                final_head.next=temp1
                temp1=temp1.next
            else:
                final_head.next=temp2
                temp2=temp2.next
            
            final_head=final_head.next
        if temp1:
            final_head.next=temp1
        elif temp2:
            final_head.next=temp2
        return head
        







        
