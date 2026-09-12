class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T={}
        F={}
        found=0
        l=0
        maximum=len(s)+1
        x_coor=0
        for i in range(len(t)):
            T[t[i]] = T.get(t[i],0)+1
        for j in range(len(s)):
            if(s[j] in T):
                F[s[j]] = F.get(s[j],0)+1
                if(T[s[j]] == F[s[j]]):
                    found+=1
            while(found == len(T)):
                if j-l+1<maximum:
                    x_coor=l
                    maximum=j-l+1
                if(s[l] in T):
                    F[s[l]]-=1
                if(s[l] in T and F[s[l]]<T[s[l]]):
                    found-=1
                l+=1
        if(maximum == len(s)+1):
            return  ""    
        return s[x_coor:x_coor+maximum]
                    



                    
            
            
                

                
            





        
