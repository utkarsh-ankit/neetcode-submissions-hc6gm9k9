#The concept is, if all are negative, the max will be not the sum but the min nagetive mumber.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        summ=float("-inf")
        current=0

        for i in nums:
            current+=i
            summ=max(summ,current)
            if current<0:
                current=0

        return summ


        