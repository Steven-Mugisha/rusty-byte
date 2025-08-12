from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # def get_neighbors()
        R, C = len(image), len(image[0])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        visited = {(sr,sc)}
        q = deque([(sr,sc)])

        if image[sr][sc] == color:
            return image

        init_color = image[sr][sc]

        while q:
            row, col = q.popleft()
            image[row][col] = color

            for dr, dc in directions:
                new_r, new_c = row + dr, col + dc
                if (new_r in range(R) and new_c in range(C) and (new_r, new_c) not in visited and image[new_r][new_c] == init_color):
                    q.append((new_r, new_c))
                    visited.add((new_r, new_c))
        
        return image

