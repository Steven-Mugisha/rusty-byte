class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            counter = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                counter[index] += 1
     
            groups[tuple(counter)].append(s)
        
        return groups.values()



        