class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the input array:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last_start,last_end = res[-1][0],res[-1][1]
            current_start, current_end = intervals[i][0], intervals[i][1]

            if current_start <= last_end:
                res[-1] = [last_start, max(current_end, last_end)]
            
            else:
                res.append([current_start, current_end])
        
        return res