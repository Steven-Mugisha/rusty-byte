class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            last_range = res[-1]
            current_range = intervals[i]

            if current_range[0] <= last_range[1]:
                res[-1] = [last_range[0], max(current_range[1], last_range[1])]
            
            else:
                res.append(intervals[i])

        
        return res 




