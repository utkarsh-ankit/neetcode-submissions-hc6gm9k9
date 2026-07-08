import heapq
import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
#sorting
        # nums.sort()
        # return nums[len(nums)-k]

#heap
        # return heapq.nlargest(k, nums)[-1]

#quick select

        k=len(nums)-k

        def quickselect(l,r):
            if l==r:
                return nums[l]

            pivot_inx=random.randint(l,r)
            nums[pivot_inx],nums[r]=nums[r], nums[pivot_inx]

            pivot,p=nums[r],l

            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p],nums[i]=nums[i], nums[p]
                    p+=1
            nums[p],nums[r]=nums[r],nums[p]

            if p>k:
                return quickselect(l,p-1)
            elif p<k:
                return quickselect(p+1,r)
            else:
                return nums[p]

        return quickselect(0, len(nums)-1)




