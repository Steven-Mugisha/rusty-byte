class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_y, min_x = m,n

        for y, x in ops:
            min_y = min(min_y, y)
            min_x = min(min_x, x)

        return min_x * min_y



