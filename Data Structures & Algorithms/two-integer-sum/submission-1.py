class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            b=target-nums[i]
            for j in range(i+1, len(nums)+1):
                if nums[j]==b:
                    return [i, nums.index(b)]
                
            