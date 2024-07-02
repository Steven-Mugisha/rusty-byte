class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # BaseCase: When equal return any number (max or min)
        # RecursiveCase: When either max or min is higher reduce it until it reaches the BaseCase.

        def gcdHelper(minVal, maxVal):
            if minVal == maxVal:
                return minVal
            
            else:
                if minVal < maxVal:
                    return gcdHelper(minVal, maxVal - minVal)
                
                else:
                    return gcdHelper(minVal - maxVal, minVal)
        
        return gcdHelper(min(nums), max(nums))