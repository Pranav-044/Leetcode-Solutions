class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        length=0
        dictionary={}
        max_f=0
        maximum=0
        for i in range(len(s)):
            length=i-l+1
            dictionary[s[i]]=dictionary.get(s[i],0)+1
            max_f=max(max_f,dictionary[s[i]])
            val=length-max_f
            if(val<=k):
                maximum=max(maximum,length)
            else:
                dictionary[s[l]]-=1
                l+=1
        return maximum
        
