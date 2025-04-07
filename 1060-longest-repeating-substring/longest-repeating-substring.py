class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        def exists(s, mid):
            chuncks_set = set()
    
            for i in range(len(s) - mid + 1):
                substring = s[i:i+mid]
                if substring in chuncks_set:
                    return True
                
                chuncks_set.add(substring)

            return False

        start, end = 0, len(s) - 1

        while start <= end:
            mid = (start + end) //2

            if exists(s, mid):
                start = mid + 1
            
            else:
                end = mid - 1
        
        return start -1