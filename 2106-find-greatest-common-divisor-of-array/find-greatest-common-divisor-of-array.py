class Solution:
    def findGCD(self, nums: List[int]) -> int:

        # iterative:
        # mn, mx = min(nums), max(nums) -> O(n)
        
        # ans = 1
        # for i in range(1, mn + 1):
        #     if mn % i == 0 and mx % i == 0:
        #         ans = i
        
        # return ans
        # TC: O(n), SC: O(1)

        # recursion:
        def gcdHelper(mn, mx):
            if mn == mx: return mn
            
            else:
                if mn < mx:
                    return gcdHelper(mn, mx - mn)
                
                else:
                    return gcdHelper(mn - mx, mx)
        
        return gcdHelper(min(nums), max(nums))
        
        
        




