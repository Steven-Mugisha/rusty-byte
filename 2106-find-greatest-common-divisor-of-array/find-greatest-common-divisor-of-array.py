class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def dfs(min_val, max_val):
            if min_val == max_val:
                return min_val
            
            elif min_val > max_val:
                return dfs(min_val - max_val, max_val)
            
            else:
                return dfs(min_val, max_val-min_val)
        
        min_val, max_val = min(nums), max(nums)

        return dfs(min_val, max_val)




    
            
