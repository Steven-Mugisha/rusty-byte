class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {val: idx for idx, val in enumerate(nums1)}

        stack = []
        res = [-1]*len(nums1)

        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = curr
            if curr in nums1Idx:
                stack.append(curr)

        return res