class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        

        dictionary={}
        j=0
        q=[]
        final=[[] for i in range(len(nums)+1)]
        for i in nums:
            dictionary[i]=dictionary.get(i,0)+1
        for l,p in dictionary.items():
            final[p].append(l)
        for m in range(len(final)-1,-1,-1):
            if(j!=k and final[m]!=[]):
                j+=len(final[m])
                q+=final[m]
        return q

        

