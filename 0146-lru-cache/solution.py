class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=self.prev=None
class LRUCache:
    def __init__(self,capacity):
        self.cap=capacity
        self.cache={}
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next=self.right
        self.right.prev=self.left
    def insert(self,node):
        previous,nxt=self.right.prev,self.right
        previous.next=nxt.prev=node
        node.next=nxt
        node.prev=previous
    def remove(self,node):
        current=node.prev
        nxt=node.next
        current.next=nxt
        nxt.prev=current
    
    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if(len(self.cache)>self.cap):
            self.key=self.left.next
            self.remove(self.left.next)
            del self.cache[self.key.key]
    
         
    


    
        

