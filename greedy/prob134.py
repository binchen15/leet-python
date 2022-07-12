class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        n = len(gas)
        balances = [ gas[i] - cost[i] for i in range(n) ]

        if sum(balances) < 0:
            return -1
            
        tot = 0
        start = 0
        for i in range(n):
            tot += balances[i]
            if tot < 0:
                tot = 0
                start = i+1
        
        return start
