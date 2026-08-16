class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        final=[]
        combo = []
        setter=set()
        candidates.sort()
        def backtrack(i,summation,substring):
            if(summation == 0):
                if(tuple(substring) not in setter):
                    setter.add(tuple(substring))
                    final.append(substring)
                return
            elif(summation<0 or i == len(candidates)):
                return
            backtrack(i+1,summation-candidates[i],substring+[candidates[i]])
            next_idx=i+1
            while(next_idx<len(candidates) and candidates[next_idx] == candidates[next_idx-1]):
                next_idx+=1
            backtrack(next_idx,summation,substring)
            
        backtrack(0,target,combo)
        return final
        
