
# 26. Remove Duplicates from Sorted Array

# Summary: Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.
# Key words: sorted, non-decreasing order, in-place, unique element, relative order

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:

        # return k as the number of unique elements 

        k = 0
        for i in nums:
            if i != nums[k-1]:
                nums[k] = i
                k += 1
        return k
    
# Example:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]