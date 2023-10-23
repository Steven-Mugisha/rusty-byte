class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

            decode = []
            for i in range(len(code)):
                if k > 0:
                    sum = 0
                    j = i+1
                    m = k
                    while(m):
                        sum+=code[j%len(code)]
                        m-=1
                        j+=1
                    decode.append(sum)

                elif k == 0:
                    decode.append(0)

                else:
                    sum = 0
                    j = i-1
                    m = k
                    while(m):
                        sum+=code[j%len(code)]
                        m+=1
                        j-=1
                    decode.append(sum)

            return decode


  





            