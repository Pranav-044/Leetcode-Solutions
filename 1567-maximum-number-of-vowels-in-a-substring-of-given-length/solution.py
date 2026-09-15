class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        setter={"a","e","i","o","u"}
        l=0
        count=0
        final=0
        for i in range(len(s)):
            if(s[i] in setter):
                count+=1
            if(i>=k):
                if(s[l] in setter):
                    count-=1
                l+=1
            final=max(final,count)
            
        return final

            




        
