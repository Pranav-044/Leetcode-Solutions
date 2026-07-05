class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        final=""
        for i in range(0,len(s),2*k):
            temp=i
            string=""
            count=0
            while(temp<len(s) and count<k):
                string+=s[temp]
                temp+=1
                count+=1
            final+=string[::-1]+s[temp:temp+k]

        return final
            
        
