class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        prof=0
        while(r<len(prices)):
            if(prices[l]>prices[r]):
                l=r
                r+=1
            else:
                calc=prices[r]-prices[l]
                prof=max(prof,calc)
                r+=1
        print(l)
        print(r)
        return prof
            




            

        
        
