class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        size = len(nums)
        for i in range(size):
            slow = fast = i
            forward = nums[i] > 0
        
            while True:
                slow = self.next_step(slow, nums[slow], size) 
                if self.is_not_cycle(nums, forward, slow):
                    break
            
                fast = self.next_step(fast, nums[fast], size)
                if self.is_not_cycle(nums, forward, fast):
                    break
                
                fast = self.next_step(fast, nums[fast], size)
                if self.is_not_cycle(nums, forward, fast):
                    break
            
                if slow == fast:
                    return True
                
        return False

    # A function to calculate the next step
    def next_step(self, pointer, value, size):
        result = (pointer + value) % size
        if result < 0:
            result += size
        return result

    # A function to detect a cycle doesn't exist
    def is_not_cycle(self, nums, prev_direction, pointer):

            curr_direction = nums[pointer] >= 0
            if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
                return True
            else:
                return False
