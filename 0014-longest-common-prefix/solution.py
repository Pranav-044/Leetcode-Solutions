class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_index=float("inf")
        for s in strs:
            if len(s)<min_index:
                min_index=len(s)


        i=0
        while i<min_index:
          for s in strs:
            if s[i]!=strs[0][i]:
                return s[:i]
          i+=1
        return s[:i]          


        
