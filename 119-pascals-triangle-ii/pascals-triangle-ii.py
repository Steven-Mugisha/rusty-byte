class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        
        else:
            line = [1]
            previousLine = self.getRow(rowIndex -1)
            for i in range(len(previousLine) - 1):
                line.append(previousLine[i] + previousLine[i+1])
            line += [1]
            
        return line
