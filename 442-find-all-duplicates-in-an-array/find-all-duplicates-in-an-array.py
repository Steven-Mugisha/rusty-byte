class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        result = []

        for n in range(len(nums)):
            get_index = abs(nums[n]) - 1
            
            if nums[get_index] < 0:
                result.append(abs(nums[n]))
            
            else:
                nums[get_index] = -1 * nums[get_index]

        return result
        
        




            
