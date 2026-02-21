class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        dictionary={}
        maximum=0
        max_f=0
        for i in range(len(s)):
            length=i-l+1
            dictionary[s[i]] = dictionary.get(s[i],0)+1
            max_f=max(max_f,dictionary[s[i]])
            if(length-max_f<=k):
                maximum=max(maximum,length)
            else:
                dictionary[s[l]]-=1
                l+=1
        return maximum
            



        
