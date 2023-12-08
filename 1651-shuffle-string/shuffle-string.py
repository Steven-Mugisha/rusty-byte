class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:

        Map = {}

        for i in range(len(s)):
            Map[indices[i]] = s[i]
        j = 0
        final_string = ''
        while j < len(indices):
          final_string += ''.join(Map[j])
          j += 1
        
        return final_string
