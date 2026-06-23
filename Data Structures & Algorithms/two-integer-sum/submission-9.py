class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #         a=nums[i]
        #         b=target-a
        #         if b in nums and nums.index(b)!=i:
        #             return [i,nums.index(b)]

        hmap={nums[i]:i for i in range(len(nums))}

        for i in range(len(nums)):
            d=target-nums[i]
            if d in hmap and hmap[d]!=i:
                return [i,hmap[d]]
                
            