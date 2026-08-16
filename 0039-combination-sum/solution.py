class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        combo = []
        def backtrack(i,summation,substring):
            if(summation<0 or i == len(candidates)):
                return
            elif(summation == 0):
                final.append(substring)
                return
            backtrack(i,summation-candidates[i],substring+[candidates[i]])
            backtrack(i+1,summation,substring)
            
        backtrack(0,target,combo)
        return final


        
