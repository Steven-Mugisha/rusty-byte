class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        pre = [1] * n
       
        for i in range(1, n):
            pre[i] = pre[i-1] * nums[i-1]
        
        # [1,1,2,6]
        

        curr_prod = 1
        for i in reversed(range(n)):
            pre[i] = pre[i] * curr_prod
            curr_prod = curr_prod * nums[i]
            print(f'curr_prod {curr_prod}')
        
        return pre
     
        


            # pre[i] = pre[i]*nums[i+1]

            #[1,2,3,4]
            # [1,1,2,6]
    

        
        # suf = [1] * n

        # for i in reversed(range(n - 1)):
        #     suf[i] = suf[i+1] * nums[i+1]
    
        # ans = []

        # for i in range(n):
        #     ans.append(pre[i]*suf[i])
        
        # return ans



        
        

        
    







