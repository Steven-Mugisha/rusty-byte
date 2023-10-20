class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        pre = nums[:n]
        post = nums[n:]
        res = []

        i = 0
        while i < len(pre):
            res.append(pre[i])
            res.append(post[i])
            i += 1
        return res

        # neat code:

        # for i in range(n):
        #     nums[i] = nums[i] << 10
        #     nums[i] = nums[i] | nums[i+n] # store x and y

        # j = 2 * n - 1
        # for i in range(n -1, -1, -1):
        #     y = nums[i] & (2**10 - 1)
        #     x = nums[i] >> 10
        #     nums[j] = y
        #     nums[j-i] = x
        #     j -= 2
        # return nums

            








