# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         #https://www.youtube.com/watch?v=Ajr8d8bgpUE watch this

#         for i in range(len(nums)):
#             if nums[i]<0:
#                 nums[i]=len(nums)+1
        
#         for j in range(len(nums)):
#             val=abs(nums[j])
#             if 1<=val<=len(nums) and nums[val-1]>0:
#                 nums[val-1]*=-1

#         for k in range(len(nums)):
#             if nums[k]>0:
#                 return k+1

#         return len(nums)+1


        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n+1  #replacing out of range values with sentinel
        
        for j in range(n):
            val = abs(nums[j])
            if 1 <= val <= n and nums[val-1] > 0:
                nums[val-1] *= -1  #marking as visited using negative
        
        for k in range(n):
            if nums[k] > 0:
                return k+1  #first unmarked index is the answer
                
        return n+1  #all 1 to n present, return n+1