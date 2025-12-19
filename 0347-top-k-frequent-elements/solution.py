class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary={}
        j=0
        final=[]
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            dictionary[n] = 1 + dictionary.get(n,0)
        for n,c in dictionary.items():
            freq[c].append(n)

        for i in range(len(freq)-1,0,-1):
            if(j!=k and freq[i]!=[]):
                j+=len(freq[i])
                final+=freq[i]
        return final[::-1]
        
