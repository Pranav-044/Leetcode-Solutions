class Solution:
    def repeatedCharacter(self, s: str) -> str:
        setter=set()
        for i in range(len(s)):
            if s[i] in setter:
                return s[i]
            setter.add(s[i])



        
        
