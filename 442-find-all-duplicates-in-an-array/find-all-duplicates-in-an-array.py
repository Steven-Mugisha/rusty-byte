class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = []
        for n in nums:
            get_index = abs(n) - 1
            nums[get_index] *= -1
            
            if nums[get_index] > 0:
                ans.append(abs(n))
        
        return ans