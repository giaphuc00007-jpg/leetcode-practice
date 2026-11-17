class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        i = 1
        while i < len(intervals):       
            before = intervals[i-1]
            now = intervals[i]
            if before[1] >= now[0]:
                before[1] = max(now[1],before[1])
                intervals.pop(i)
            elif before[1] < now[0]:
                i += 1
        return intervals

