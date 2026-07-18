class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res=0
        # cur_sum=0
        # pre_sum={0:1}

        # for n in nums:
        #     cur_sum+=n
        #     diff=cur_sum-k

        #     res+=pre_sum.get(diff,0)
        #     pre_sum[cur_sum]=1+pre_sum.get(cur_sum,0)
        
        # return res

        res=0
        cur_sum=0
        pre_sum={0:1}

        for n in nums:
            cur_sum+=n
            diff=cur_sum-k

            res+=pre_sum.get(diff,0)
            pre_sum[cur_sum]=1+pre_sum.get(cur_sum,0)

        return res

            



        