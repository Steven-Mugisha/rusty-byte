class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        run_sum = []
        total_sum = 0

        for i in nums:
          total_sum += i
          run_sum.append(total_sum)

        return run_sum

        
       

