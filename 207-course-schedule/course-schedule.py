class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = defaultdict(list)

        for crs, preq in prerequisites:
            courses[crs].append(preq)
        
        visiting, seen = set(), set()

        def has_cycle(course):
            if course in visiting:
                return True
            
            if course in seen:
                return False
            
            visiting.add(course)
            for preq in courses[course]:
                if has_cycle(preq):
                    return True
            visiting.remove(course)
            seen.add(course)
            return False

        for preq in range(numCourses):
            if has_cycle(preq):
                return False
        
        return True