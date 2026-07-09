class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #https://www.youtube.com/watch?v=Ajr8d8bgpUE watch this

        for i in range(len(nums)):
            if nums[i]<=0:
                nums[i]=len(nums)+1
        
        for j in range(len(nums)):
            val=abs(nums[j])
            if 1<=val<=len(nums) and nums[val-1]>0:
                nums[val-1]*=-1

        for k in range(len(nums)):
            if nums[k]>0:
                return k+1

        return len(nums)+1


        