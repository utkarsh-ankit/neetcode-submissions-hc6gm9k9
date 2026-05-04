"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        ordered=sorted(intervals, key=lambda x:x.start)
        i=0
        rooms=0

        while i<len(ordered)-1:
            if ordered[i].end>ordered[i+1].start:
                rooms+=1
                i+=1
            else:
                i+=1
        return i if len(ordered)>1 else 1



        