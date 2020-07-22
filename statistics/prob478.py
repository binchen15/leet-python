class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        import random
        ub = self.radius * self.radius
        xl, xr = self.x_center - self.radius, self.x_center + self.radius
        yl, yr = self.y_center - self.radius, self.y_center + self.radius 
        while True:
            x = random.uniform(xl, xr)
            y = random.uniform(yl, yr)
            d2 = (x - self.x_center) * (x - self.x_center)  + \
                 (y - self.y_center) * (y - self.y_center) 
            if d2 <= ub:
                return [x, y]


