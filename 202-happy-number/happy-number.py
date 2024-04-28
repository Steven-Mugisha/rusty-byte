class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquare(number):
            totalSum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                totalSum += digit**2
            return totalSum
        
        slowPointer = n
        fastPointer = sumSquare(n)

        while slowPointer != fastPointer and fastPointer != 1:
            slowPointer = sumSquare(slowPointer)
            fastPointer = sumSquare(sumSquare(fastPointer))
        
        if fastPointer == 1:
            return True
        
        return False