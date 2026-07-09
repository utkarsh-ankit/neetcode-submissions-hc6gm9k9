class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort() #imp step

        for i, a in enumerate(nums):
            if a>0:
                break #because all all positive number, so no sol

            if i>0 and a==nums[i-1]: #repetition observe
                continue

            l,r=i+1,len(nums)-1 #two pointers

            while l<r:
                ts=a+nums[l]+nums[r]
                if ts>0:
                    r-=1
                elif ts<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res



        