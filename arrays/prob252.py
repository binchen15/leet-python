class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        m = len(intervals)
        if m <= 1:
            return True

        intervals.sort()
        for i in range(1, m):
            prev = intervals[i-1]
            curr = intervals[i]
            if curr[0] < prev[1]:
                return False

        return True
