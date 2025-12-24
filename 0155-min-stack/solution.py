class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        stack1=self.stack.copy()
        mini=stack1[-1]
        while(len(stack1)):
            mini=min(mini,stack1[-1])
            stack1.pop()
        return mini
