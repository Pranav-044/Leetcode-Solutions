class Solution:
    def isValid(self, s: str) -> bool:
        mapping={"}":"{","]":"[",")":"("}
        stack=[]
        for i in s:
            if i in mapping:
                if stack:
                    element=stack.pop()
                    if mapping[i] !=element:
                        return False 
                else:
                    return False
            else:
                stack.append(i)
        return not stack



        
