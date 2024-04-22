class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for crs, preq in prerequisites:
            courses[crs].append(preq)
        
        visiting, seen = set(), set()
        
        def has_cycle(crs):
            if crs in visiting:
                return True
            
            if crs in seen:
                return False

            visiting.add(crs)
            for preq in courses[crs]:
                if has_cycle(preq):
                    return True
                
            visiting.remove(crs)
            seen.add(crs)
            return False
        
        for cr in range(numCourses):
            if has_cycle(cr):
                return False
            
        return True