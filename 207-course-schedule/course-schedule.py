class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = collections.defaultdict(list)

        for cr, preq in prerequisites:
            courses[cr].append(preq)
        
        visiting_edges, seen_vertex = set(), set()
        
        def has_cycle(course):
            if course in visiting_edges:
                return True

            if course in seen_vertex:
                return False
            
            visiting_edges.add(course)
            for preq in courses[course]:
                if has_cycle(preq):
                    return True
            visiting_edges.remove(course)
            seen_vertex.add(course)
            return False

        for cr in range(numCourses):
            if has_cycle(cr):
                return False
        return True