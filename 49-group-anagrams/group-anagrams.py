class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        groups = defaultdict(list)

        for exp in strs:
            count = [0]*26
            for c in exp:
                index = ord(c) - ord('a')
                count[index] += 1
            
            groups[tuple(count)].append(exp)
        
        return list(groups.values())
    
        

