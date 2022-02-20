class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        if k == 1:
            return n
        
        friends = [ i for i in range(1, n+1)]
        
        i = 0
        while friends:
            
            m = len(friends)
            if m == 1:
                return friends[0]  # the winner
            
            for j in range(k-1):
                i = (i + 1) % len(friends)
                
            friends.pop(i)
            i = i % len(friends)
