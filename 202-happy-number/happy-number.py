class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(number):
            totalSum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                totalSum += digit**2
            return totalSum
        
        slow = n
        fast = squares(n)

        while fast != slow and fast != 1:
            slow = squares(slow)
            fast = squares(squares(fast))

        if fast == 1:
            return True
        
        return False
    