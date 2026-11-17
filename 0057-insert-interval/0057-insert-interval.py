class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort()
        i = 1 
        while i < len(intervals):
            before = intervals[i-1]
            now = intervals[i]
            if before[1] >= now[0]:
                before[1] = max(now[1],before[1])
                intervals.pop(i)
            else:
                i+= 1
        return intervals