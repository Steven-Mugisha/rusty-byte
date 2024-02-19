class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l,r = 0, len(numbers) - 1

        while l < r:
            if (numbers[l] + numbers[r]) < target:
                l += 1
            elif (numbers[l] + numbers[r]) > target:
                r -= 1
            
            else:
                return [l+1, r+1]

        # while r <= len(numbers):
        #     if (numbers[l] + numbers[r]) == target:
        #         return [l+1, r+1]
        #     else:
        #         for i in range(r+1, len(numbers)):
        #             if (numbers[l] + numbers[i]) == target:
        #                 return [l+1, i+1]
        #         l += 1
        #     r += 1
        