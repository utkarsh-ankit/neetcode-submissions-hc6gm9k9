import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        a=[]
        c=[]
        for i in range(len(points)):
            b=math.sqrt((points[i][0])**2+(points[i][1])**2)
            a.append((-1*b,i))
        
        b=heapq.nlargest(k,a)
        for j,l in b:
            c.append(points[l])
        return c
        
        