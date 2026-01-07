"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr=head
        dictionary={}
        if not head:
            return None
        while curr:
            temp=Node(curr.val)
            dictionary[curr] = temp
            curr=curr.next
        curr=head
        while curr:
            copy_node=dictionary[curr]
            if(curr.next):
                copy_node.next=dictionary[curr.next]
            if curr.random:
                copy_node.random=dictionary[curr.random]
            curr=curr.next
        return dictionary[head]
        
            

        
