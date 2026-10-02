class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        p_dict={}
        s_dict={}
        l=0
        count=[]
        for i in p:
            p_dict[i] = p_dict.get(i,0)+1
        for j in range(len(s)):
            print(s_dict)
            s_dict[s[j]] = s_dict.get(s[j],0)+1
            if(j>=len(p)):
                s_dict[s[l]]-=1
                if(s_dict[s[l]] == 0):
                    s_dict.pop(s[l])
                l+=1
            if(s_dict == p_dict):
                count.append(l)
        return count
            
        