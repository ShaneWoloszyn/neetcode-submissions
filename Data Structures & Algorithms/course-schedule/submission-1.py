class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = {i:[] for i in range(numCourses)}


        for crs, preq in prerequisites:
            courses[crs].append(preq)
            
        visit = set()
        def search(crs):
            if crs in visit:
                return False
            if courses[crs] == []:
                return True
            
            visit.add(crs)
            for preq in courses[crs]:
                if not search(preq):
                    return False
            visit.remove(crs)
            courses[crs] = []
            return True
        
        for i in range(numCourses):
            if not search(i):
                return False
        
        return True
                