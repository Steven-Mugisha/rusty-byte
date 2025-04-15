class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        
        left_arr = [height[0]]*n
        right_arr = [height[-1]]*n

        for i in range(1, n):
            left_arr[i] = max(height[i], left_arr[i -1])

        for i in range(n - 2, -1, -1):
            right_arr[i] = max(height[i], right_arr[i + 1])

        trapped_water = sum(min(left_arr[i], right_arr[i]) - height[i] for i in range(n))

        return trapped_water 