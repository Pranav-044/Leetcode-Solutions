class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        arr = sorted(position)

        if m == 2:
            return arr[-1] - arr[0]

        def isPossible(value):
            count = 2
            last = 0
            for i in range(1, len(arr)-1):
                if arr[i] - arr[last] >= value:
                    count += 1
                    last = i
                    if(arr[-1] - arr[i]<value):
                        count-=1

            return count >= m

        l = 1
        r = arr[-1] - arr[0]
        maximum = 1

        while l <= r:
            mid = (l + r) // 2
            if isPossible(mid):
                maximum = mid
                l = mid + 1
            else:
                r = mid - 1

        return maximum

            

        
