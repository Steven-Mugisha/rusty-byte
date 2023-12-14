class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        rows = [[1]]

        for i in range(rowIndex):
            curr = [0] + rows[-1] + [0]
            new_row = []
            for j in range(len(curr) -1):
                sum_val = curr[j] + curr[j+1]
                new_row.append(sum_val)
            rows.append(new_row)
        
        return rows[-1]
        