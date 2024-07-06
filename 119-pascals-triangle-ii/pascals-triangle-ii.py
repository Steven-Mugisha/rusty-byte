class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        stack = [[1]]
        if rowIndex == 0:
            return stack[-1]
        
        for i in range(1, rowIndex + 1):
            temp_arr = [1]
            lastLine = stack[-1]
            for j in range(len(lastLine) - 1):
                temp_arr.append(lastLine[j] + lastLine[j+1])
            temp_arr += [1]
            stack.append(temp_arr)
        
        return stack[-1]
        

    