class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)+len(nums2)
        if n%2==0:
            return (n+1)/2
        else:
            return (n/2+((n/2)+1))/2
        