class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return self.gcdHelper(min(nums), max(nums))
    

    def gcdHelper(self, minValue, maxValue):
        if minValue == maxValue:
            return maxValue
        
        else:
            if maxValue > minValue:
                return self.gcdHelper(minValue, maxValue - minValue)
            
            return self.gcdHelper(minValue - maxValue, maxValue)
    
        