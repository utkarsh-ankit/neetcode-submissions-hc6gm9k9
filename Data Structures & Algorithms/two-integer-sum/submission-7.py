class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #         a=nums[i]
        #         b=target-a
        #         if b in nums and nums.index(b)!=i:
        #             return [i,nums.index(b)]

        hmap={nums[i]:i for i in range(len(nums))}
        for j in range(len(nums)):
            k=target-nums[j]
            if k in hmap and hmap[k]!=j:
                return [j,hmap[k]]
                
            