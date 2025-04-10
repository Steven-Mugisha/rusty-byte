class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g.sort(), s.sort()
        content_child, cookie_index = 0, 0
        ans = 0

        while content_child < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[content_child]:
                content_child += 1
            cookie_index += 1
        return content_child
    
            


