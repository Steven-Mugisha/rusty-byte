class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        general_prefix = strs[0]

        for i in range(1, len(strs)):
            temp_prefix = ""
            curr_str = strs[i]

            for i in range(len(list(curr_str))):
                if (i < len(general_prefix)) and (general_prefix[i] == curr_str[i]):
                    temp_prefix += curr_str[i]
                elif  (i < len(general_prefix)) and (general_prefix[i] != curr_str[i]):
                    break
            general_prefix = temp_prefix
        
        return general_prefix
