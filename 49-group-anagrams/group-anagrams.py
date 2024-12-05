class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        groups = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            groups[tuple(count)].append(s)
        
        return list(groups.values())