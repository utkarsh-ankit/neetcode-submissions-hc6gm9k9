class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        b=len(nums)*[0]
        for i in nums:
            a*=i
        if a==0 and nums.count(0)>=2:
            return b
        elif a==0 and nums.count(0)==1:
            c=nums.index(0)
            e=d=1
            for e in nums[:c+1]:
                e*=e
            for d in nums[c:]:
                d*=d
            b[c]=e*d
            return b
        else:
            for j in range(len(b)):
                b[j]=(a//nums[j])
        return b
        


                

