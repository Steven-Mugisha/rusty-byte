class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last_start, last_end = res[-1][0], res[-1][1]
            curr_start, curr_end = intervals[i][0], intervals[i][1]

            if curr_start <= last_end:
                res[-1] = [last_start, max(last_end, curr_end)]
            
            else:
                res.append([curr_start, curr_end])
        
        return res