class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l, r = 0, 0

        count_ones = 0
        shortest_length = float("inf")
        ans = []

        while r < len(s):
            if s[r] == '1':
                count_ones += 1
            
            while count_ones == k:
                current_length = r - l + 1
                if current_length <= shortest_length:
                    if current_length < shortest_length:
                        ans.clear()
                    shortest_length = current_length
                    ans.append(s[l:r + 1])

                if s[l] == '1':
                    count_ones -= 1
                
                l += 1
                
            r += 1
        
        if not ans:
            return ""
        
        return min(ans)
