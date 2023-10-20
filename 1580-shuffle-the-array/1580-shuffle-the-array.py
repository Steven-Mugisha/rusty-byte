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

            








