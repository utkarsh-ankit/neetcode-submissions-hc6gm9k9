class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)
        while i<=j:
            mid=(i+j)//2
            if target<nums[mid]:
                r=mid
            elif target>nums[mid]:
                l=mid
            return mid if target==nums[mid] else -1



























        # l=0
        # r=len(nums)-1

        # while l<=r:
        #     mid=l+(r-l)//2
            
        #     if target>nums[mid]:
        #         l=mid+1
        #     elif target<nums[mid]:
        #         r=mid-1
        #     else:
        #         return mid
        # return -1