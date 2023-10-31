class Solution:
    def isHappy(self, n: int) -> bool:
        Seen = set()

        while n not in Seen:
            Seen.add(n)
            n = self.SumOfSquares(n)
            if n == 1:
                return True
        return False
    
    def SumOfSquares(self, n:int) -> int:
        res = 0
        while n:
            digit = n%10
            digit = digit**2
            res += digit
            n = n//10
        return res 

            