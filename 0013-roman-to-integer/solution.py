class Solution:
    def romanToInt(self, s: str) -> int:
        val={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        summation=val[s[0]]
        check=("I","X","C")
        for i in range(1,len(s)):
            if(val[s[i]]>val[s[i-1]]):
                summation+=(val[s[i]] - 2*val[s[i-1]])
            else:
                summation+=val[s[i]]
        return summation
            
            

        
