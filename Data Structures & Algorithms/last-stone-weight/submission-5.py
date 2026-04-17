import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            if len(stones)>=2:
                a=stones[-1]-stones[-2]
                stones.pop()
                stones.pop()
                stones.append(a)
                stones.sort()
            else:
                return stones[0]
        return a

        