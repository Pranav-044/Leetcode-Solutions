class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for i in range(len(tokens)):
            if(tokens[i] in ["+","-","*","/"]):
                popped=[]
                r=0
                while stack and r<2:
                    popped.append(stack.pop())
                    r+=1
                if(tokens[i] == "+"):
                    if(popped):
                        stack.append(popped[-1]+popped[0])
                elif(tokens[i] == "*"):
                    if(popped):
                        stack.append(popped[-1]*popped[0])
                elif(tokens[i] == "/"):
                    if(popped):
                        stack.append(int(popped[-1]/popped[0]))
                elif(tokens[i] == "-"):
                    if(popped):
                        stack.append(popped[-1]-popped[0])
            else:
                stack.append(int(tokens[i]))
        return stack[-1]
        
