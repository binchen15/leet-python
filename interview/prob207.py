class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        from collections import defaultdict
        
        dep = defaultdict(set)
        
        for a, b in prerequisites:
            dep[a].add(b)  # a dependes on b
            
        courses = set(i for i in range(numCourses))
        
        while True:
            dependent = dep.keys()
            if not dependent:
                return True
            independent = courses - set(dependent)  # course you can take
            if not independent:
                return False
            
            courses.difference_update(independent)
            
            for key in independent:
                for key2 in dep:
                    if key in dep[key2]:
                        dep[key2].remove(key)
                
            toremove = set()
            for key in dep:
                if not dep[key]:
                    toremove.add(key)
                    
            for key in toremove:
                del dep[key]
