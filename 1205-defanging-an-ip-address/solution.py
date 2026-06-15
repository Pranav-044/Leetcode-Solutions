class Solution:
    def defangIPaddr(self, address: str) -> str:
        final=""
        for i in address:
            if i==".":
                final+="[.]"
            else:
                final+=i
        return final
        
