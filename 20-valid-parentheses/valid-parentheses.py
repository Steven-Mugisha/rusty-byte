class Solution:
    def isValid(self, s: str) -> bool:
        Map = {
            ')': '(',
            ']' : '[',
            '}' : '{'
            }
        
        stack  = []

        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            elif len(stack) == 0 or stack.pop() != Map[b]:
                return False
        return len(stack) == 0





        







       






    




    
        


         

    


            
            

        

         

