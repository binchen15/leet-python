class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        
        col = ord(coordinates[0]) - ord('a') + 1 
        row = int(coordinates[1])
        
        return (row + col) % 2 == 1
