# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return None
        curr1=l1
        curr2=l2
        num1=""
        num2=""
        final=ListNode(-100)
        head=final
        while curr1:
            num1+=str(curr1.val)
            curr1=curr1.next
        while curr2:
            num2+=str(curr2.val)
            curr2=curr2.next
        res1=num1[::-1]
        res2=num2[::-1]
        res=str(int(res1)+int(res2))[::-1]
        for i in range(len(res)):
            temp=ListNode(int(res[i]))
            final.next=temp
            final=final.next
        return head.next
        
        
        

        
