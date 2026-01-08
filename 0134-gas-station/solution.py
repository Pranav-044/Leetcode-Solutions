class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        initial_gas=0
        start=0
        for i in range(len(gas)):
            diff=gas[i]-cost[i]
            total+=diff
            initial_gas+=diff
            if(initial_gas<0):
                start=i+1
                initial_gas=0
        if(total>=0):
            return start
        else:
            return -1

        
