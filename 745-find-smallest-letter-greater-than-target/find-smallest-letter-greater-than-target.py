class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:


        """

        letters = ["c","f","j"], target = "a"
        T T T


        
        
        
        """



        
        l, r = 0, len(letters) -1
        boundary = ''

        while l <= r:
            mid = (r + l) // 2
            if letters[mid] > target:
                boundary = letters[mid]
                r = mid - 1
            
            else:
                l = mid + 1
        
        if boundary > target:
            return boundary
        else:
            return letters[0]

