class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        runList = []
        
        rev_nums = nums[::-1]
        max_sum = sum(nums)
        runList.append(max_sum)

        print(rev_nums)

        for i in range(1, len(rev_nums)):
            res_val = runList[-1] - rev_nums[i-1]
            runList.append(res_val)
    
        return runList[::-1]


