class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
    
        smallest_val = float('-inf')
        nums = [smallest_val] + nums + [smallest_val]
        n = len(nums)

        for i in range(1, n - 1):
            if (nums[i-1] < nums[i]) and (nums[i] > nums[i + 1]):
                print(f' the values of i {i} from nums : {nums[i]}')
                return i - 1
        return 0