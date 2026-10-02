class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        final=[]
        def backtrack(left,right,string):
            nonlocal final
            if(left == n and right == n):
                final.append("".join(string))
                return
            if left<n:
                backtrack(left+1,right,string+["("])
            if(right<left):
                backtrack(left,right+1,string+[")"])
        backtrack(0,0,[])
        return final
        