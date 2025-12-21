class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check=set()
        l=0
        res=0
        for i in range(len(s)):
            while s[i] in check:
                check.remove(s[l])
                l+=1
            check.add(s[i])
            res=max(res,i-l+1)
        return res

