class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            res=sum([ceil(i/mid) for i in piles])
            if(res>h):
                l=mid+1
            elif(res<=h):
                r=mid
        return l
        
