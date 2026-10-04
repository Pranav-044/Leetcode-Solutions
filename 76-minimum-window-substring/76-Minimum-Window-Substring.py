class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t={}
        dict_s={}
        count=0
        length=float("inf")
        l=0
        start=0
        for i in t:
            dict_t[i]=dict_t.get(i,0)+1
        for j in range(len(s)):
            dict_s[s[j]] = dict_s.get(s[j],0)+1
            if(s[j] in dict_t and dict_s[s[j]] == dict_t[s[j]]):
                count+=1
            if(count == len(dict_t)):
                    while(count == len(dict_t)):
                        
                        if j-l+1<length:
                            length=j-l+1
                            start=l
                        dict_s[s[l]]-=1
                        if(s[l] in dict_t and dict_s[s[l]]<dict_t[s[l]]):
                            count-=1
                        l+=1
                    
                
        return s[start:start+length] if length!=float("inf") else ""


        #your code goes here