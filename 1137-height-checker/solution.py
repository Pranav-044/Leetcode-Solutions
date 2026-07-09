class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=[0]*101
        for i in range(len(heights)):
            count[heights[i]]+=1
        pointer=0
        j=0
        final=0
        while pointer<len(count) and j<len(heights):
            if(count[pointer] == 0):
                pointer+=1
            else:
                if(heights[j] == pointer):
                    count[pointer]-=1
                    j+=1
                else:
                    final+=1
                    j+=1
                    count[pointer]-=1
        return final


        

