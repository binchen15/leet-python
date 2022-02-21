class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        from collections import defaultdict
        
        dep = defaultdict(set)
        
        for a, b in prerequisites:
            dep[a].add(b)  # a depends on b
            
        courses = set(i for i in range(numCourses))
        orders = []
        
        while True:
            
            courses_dep = set(dep.keys())
            courses_indep = courses - courses_dep
            
            # takes those independent courses now
            orders.extend(list(courses_indep))
            courses = courses_dep
            
            if not courses_dep:
                return orders
            
            if not courses_indep:
                return []   # failed

            for key in courses_indep:
                for key2 in dep:
                    if key in dep[key2]:
                        dep[key2].remove(key)
                        
            toremove = set()
            for key in dep:
                if not dep[key]:
                    toremove.add(key)
                    
            for key in toremove:
                del dep[key]
