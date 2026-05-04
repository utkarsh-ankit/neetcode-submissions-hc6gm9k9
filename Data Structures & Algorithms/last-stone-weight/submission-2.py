import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while stones:
            a=stones[-1]-stones[-2]
            if len(stones)>2:
                stones.pop()
                stones.pop()
                stones.append(a)
                stones.sort()
            else:
                return a
        return a

        