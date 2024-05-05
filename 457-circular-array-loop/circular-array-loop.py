class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)

        def nextStep(pointer, value, size):
            step = (pointer + value) % size
            if step < 0:
                step += size
            return step

        def isNotCycle(nums, PreDirection, pointer):
            currentDirection = nums[pointer] >= 0
            if (currentDirection != PreDirection) or (abs(nums[pointer]) % len(nums) == 0):
                return True
            
            return False

        for i in range(size):
            slow = fast = i
            forward = nums[i] > 0

            while (True):
                slow = nextStep(slow, nums[slow], size)
                if isNotCycle(nums, forward, slow):
                    break
                
                fast = nextStep(fast, nums[fast], size)
                if isNotCycle(nums, forward, fast):
                    break
                
                fast = nextStep(fast, nums[fast], size)
                if isNotCycle(nums, forward,fast):
                        break
                
                if slow == fast:
                    return True
        
        return False

            