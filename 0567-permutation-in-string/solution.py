class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        string1=[0]*26
        string2=[0]*26
        for i in range(len(s1)):
            string1[ord(s1[i])-ord('a')]+=1
        for j in range(len(s2)):
            string2[ord(s2[j])-ord('a')]+=1
            if(j>=len(s1)):
                string2[ord(s2[j-len(s1)])-ord('a')]-=1
            if(string1==string2):
                return True
        return False
        
