class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        # Notice it's l < r, not l <= r. This stops when they meet.
        while l < r:
            mid = (l + r) // 2
            
            # If mid is odd, step back one space to make it even.
            # Now mid is ALWAYS the start of a pair.
            if mid % 2 == 1:
                mid -= 1
            
            # If the pair matches, the single element is to the right
            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            
            # If the pair is broken, the single element is here or to the left
            else:
                r = mid
                
        # When l and r meet, you've found the single element
        return nums[l]
