class Solution:
    def shortestPalindrome(self, s: str) -> str:
        prefix=0
        suffix=0
        base=29
        power=1
        min_index=0
        mod=10**9+7
        for i,c in enumerate(s):
            char=(ord(c)-ord("a"))+1
            prefix=(prefix*base)%mod
            prefix=(prefix+char)%mod
            suffix=(suffix+power*char)%mod
            power=(power*base)%mod
            if(suffix == prefix):
                min_index=i
        return s[min_index+1:][::-1]+s



