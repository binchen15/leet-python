class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        self.seats = capacity
        self.pq = []
        
        class Trip:
            def __init__(self, trip):
                self.trip = trip
                
            def __lt__(self, other):
                """based on offboarding position"""
                return self.trip[2] < other.trip[2]
        
        
        trips.sort(key = lambda x : x[1]) # sort by onboarding position
        
        for trip in trips:
            loc = trip[1]
            while len(self.pq) > 0 and self.pq[0].trip[2] <= loc:
                T = heapq.heappop(self.pq)
                self.seats += T.trip[0]
            
            if self.seats < trip[0]:
                return False
            
            self.seats -= trip[0]
            heapq.heappush(self.pq, Trip(trip))
            
        return True
