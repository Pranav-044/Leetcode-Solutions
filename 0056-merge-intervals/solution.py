class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final=[]
        intervals.sort()
        count=0
        final.append(intervals[0])
        for i in range(1,len(intervals)):
            if(intervals[i][0]<=final[count][1]):
                    final[count][1] = max(intervals[i][1],final[count][1])
            else:
                final.append(intervals[i])
                count+=1
        return final

        
