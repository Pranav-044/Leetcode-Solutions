class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        minimum=0
        ans=r
        while l<=r:
            mid=(l+r)//2
            minimum=sum([math.ceil(i/mid) for i in piles])
            if(minimum>h):
                l=mid+1
            elif(minimum<=h):
                ans=mid
                r=mid-1
        return ans
        
