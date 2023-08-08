
# 27. Remove Element
# summary: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed.
# key words: integer array, integer val, remove all occurrences, in-place, relative order

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        k = 0
        for i in nums:
            if i != val:
                nums[k] = i
                k +=1 
        return k 
    
# Example:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
     
