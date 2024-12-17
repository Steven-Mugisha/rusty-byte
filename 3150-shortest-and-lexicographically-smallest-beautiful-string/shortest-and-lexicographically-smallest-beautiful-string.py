class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l, r = 0, 0
        ones_count = 0
        shortest_length = float('inf')
        ans = []

        while r < len(s):
            if s[r] == '1':
                ones_count += 1

            while ones_count == k:  # Valid substring
                current_length = r - l + 1
                if current_length <= shortest_length:
                    if current_length < shortest_length:
                        ans.clear()  # Clear previous results if a shorter length is found
                    shortest_length = current_length
                    ans.append(s[l:r + 1])

                if s[l] == '1':
                    ones_count -= 1

                l += 1

            r += 1

        if not ans:
            return ""

        # Return lexicographically smallest substring
        return min(ans)
