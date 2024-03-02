class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for c in operations:
            if c == '+':
                scores.append(scores[-2] + scores[-1])
            elif c == 'C':
                scores.pop()
            elif c == 'D':
                scores.append(scores[-1] * 2)
            
            else:
                scores.append(int(c))

        return sum(scores)
            
            
        