class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n = len(image)
        
        def flip(i):
            """flip the row image[i]"""
            l, r = 0, n-1
            while l < r:
                image[i][l], image[i][r] = image[i][r], image[i][l]
                l += 1
                r -= 1
                
        def invert(i):
            """invert the row image[i]"""
            for j in range(n):
                image[i][j] ^= 1
                
        for i in range(n):
            flip(i)
            invert(i)
            
        return image
