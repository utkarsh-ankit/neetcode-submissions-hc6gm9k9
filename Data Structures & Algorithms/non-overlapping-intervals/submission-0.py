class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count=0
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                count+=1
            else:
                count+=0
        return count

        