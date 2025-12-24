class Solution:
    def isValid(self, s: str) -> bool:
        mapping={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i in mapping:
                if(not stack):
                    popped="#"
                else:
                    popped=stack.pop()
                if(mapping[i]!=popped):
                    return False
            else:
                stack.append(i)
        return not stack
                    
                

        
