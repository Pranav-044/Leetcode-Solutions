class Solution:
    def firstUniqChar(self, s: str) -> int:
        l=0
        dictionary={}
        for i in s:
            dictionary[i] = dictionary.get(i,0)+1
        for i in range(len(s)):
            if(dictionary[s[i]] == 1):
                return i
        return -1 

        
