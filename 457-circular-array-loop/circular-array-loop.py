class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)

        def next_value(pointer, value, size):
            step = (pointer + value) % size
            if step < 0:
                step += size
            return step
            

        def is_not_cycle(nums, prev_direction, pointer):
            current_direction = nums[pointer] >= 0
            if (current_direction != prev_direction) or (abs(nums[pointer]) % len(nums) == 0):
                return True
            return False

        for i in range(size):
            slow = fast = i
            forward = nums[i] > 0

            while (True):
                slow = next_value(slow, nums[slow], size)
                if is_not_cycle(nums, forward, slow):
                    break
                
                fast = next_value(fast, nums[fast], size)
                if is_not_cycle(nums, forward, fast):
                    break
                
                fast = next_value(fast, nums[fast], size)
                if is_not_cycle(nums, forward, fast):
                    break
                
                if slow == fast:
                    return True
        
        return False