class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        int_x = [(rec1[0], rec1[2]), (rec2[0], rec2[2])]
        int_y = [(rec1[1], rec1[3]), (rec2[1], rec2[3])]
        
        int_x.sort()
        int_y.sort()
        
        return int_x[0][1] > int_x[1][0] and int_y[0][1] > int_y[1][0]
