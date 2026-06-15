class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        for i in range(len(candies)):
            if (candies[i]+extraCandies)>=maximum:
                candies[i]=True
            elif (candies[i]+extraCandies)<maximum:
                candies[i]=False
        return candies
        
