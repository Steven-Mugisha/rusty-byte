class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set = set(nums)
        res = 0

        for n in nums:
            if (n-1) not in Set:
                length = 1
                while (n+length) in Set:
                    length += 1
                res = max(res, length)
        
        return res