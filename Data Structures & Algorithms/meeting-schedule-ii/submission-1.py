"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = []
        end = []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start = sorted(start)
        end = sorted(end)

        s, e = 0, 0
        count = 0
        minRooms = 0

        while s <= len(end) - 1:
            if end[e] <= start[s]:
                count -= 1
                e += 1
            else:
                count += 1
                s += 1
            if count > minRooms:
                minRooms = count
     
        return minRooms
