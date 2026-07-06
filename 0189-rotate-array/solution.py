class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        l=0
        r=len(nums)-1
        while(l<=r):
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        nums[:(k%len(nums))]=nums[:k%len(nums)][::-1]
        nums[(k%len(nums)):]=nums[k%len(nums):][::-1]
        return nums

