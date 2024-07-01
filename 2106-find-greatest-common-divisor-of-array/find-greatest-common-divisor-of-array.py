class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcdHelper(minVal, maxVal):
            if minVal == maxVal:
                return minVal
            
            elif maxVal > minVal:
                return gcdHelper(minVal, maxVal -  minVal)
            
            else:
                return gcdHelper(minVal -  maxVal, maxVal)
        
        return gcdHelper(min(nums), max(nums))
        