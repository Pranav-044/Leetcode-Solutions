class Solution:
    def minWindow(self, s: str, t: str) -> str:
        T={}
        S={}
        have=0
        l=0
        r=0
        final=[]
        final_length=float("inf")
        for i in range(len(t)):
            T[t[i]] = T.get(t[i],0)+1
        need=len(T)
        for j in range(len(s)):
            S[s[j]] = S.get(s[j],0)+1
            if s[j] in T and S[s[j]] == T[s[j]]:
                have+=1
            while have == need:
                if(j-l+1<final_length):
                    final=[l,j]
                    final_length=j-l+1
                S[s[l]]-=1
                if s[l] in T and S[s[l]]<T[s[l]]:
                    have-=1
                l+=1
        if(final_length==float("inf")):
            return ""
        else:
            l,r=final    
            return str(s[l:r+1])
        
