class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # find the index j such that nums1[i] == nums2[j]
        # determine the next greater element of nums2[j] in nums2: return it or otherwise return -1.

        # create a hash map to store the values of nums2 so that we can keep track of the indexs
        # do a for loop until the length of nums1 
        # check if there exist and element from the nums2[j] +1 if then return else return -1
        # append to res arr and then return.

        # create the map for to keep nums2 values:

        Map = {}

        for idx, val in enumerate(nums1):
            Map[val] = idx

        res = [-1]*len(nums1)
        stack = []

        # Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
        for i in range(len(nums2)):
            curr = nums2[i]
            while stack and stack[-1] < curr:
                val = stack.pop()
                index = Map[val]
                res[index] = curr
            
            if curr in Map:
                stack.append(curr)

        return res
        # for i in range(len(nums1)):
        #     val = nums1[i]
        #     if val in Map:
        #         idx = Map[val]
        #         for j in range(idx + 1, len(nums2)):
        #             if nums2[j] > val:
        #                 res[i] = nums2[j]
        #                 break
                    
        #             else:
        #                 continue
        
        # return res

        




        

       

