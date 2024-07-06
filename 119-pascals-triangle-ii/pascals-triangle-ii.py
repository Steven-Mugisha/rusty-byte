class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        else:
            line = [1]
            prevRow = self.getRow(rowIndex -1)
            for i in range(len(prevRow) - 1):
                line.append(prevRow[i] + prevRow[i+1])
            line += [1]
        
        return line