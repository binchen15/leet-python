class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans = []
        m   = len(T)
        i   = 0
        while i < m:
            j = i + 1
            while j < m and T[j] <= T[i]:
                j += 1
            if j < m: # second cond failed
                ans.append(j-i)
            else:
                ans.append(0)
            i += 1
        return ans


class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        m   = len(T)
        if m == 0:
            return []
        if m == 1:
            return [0]

        ans = []
        min_stack = []
        for i, t in enumerate(T):
            while min_stack and t > min_stack[-1][1]:
                d = min_stack[-1]
                ans.append( (d[0], i-d[0]) )
                del min_stack[-1]
            min_stack.append((i, t))
        while min_stack:  # unsolved cases
            d = min_stack[-1]
            ans.append( (d[0], 0) )
            del min_stack[-1]
        ans.sort(key = lambda x : x[0])
        return [ x[1] for x in ans]

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        m   = len(T)
        if m == 0:
            return []
        if m == 1:
            return [0]

        ans = []
        min_stack = []
        for i, t in enumerate(T):
            while min_stack and t > min_stack[-1][1]:
                d = min_stack[-1]
                ans.append( (d[0], i-d[0]) )
                del min_stack[-1]
            min_stack.append((i, t))  
        while min_stack:  # unsolved cases
            d = min_stack[-1]
            ans.append( (d[0], 0) )  
            del min_stack[-1]
        ans.sort(key = lambda x : x[0])
        return list(map(lambda x : x[1], ans))

class Solution(object):
    """96% solution."""
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        m  = len(T)
        if m == 0:
            return []
        if m == 1:
            return [0]

        ans = [0] * m
        min_stack = []
        for i, t in enumerate(T):
            while min_stack and t > T[min_stack[-1]]:
                d = min_stack[-1]
                ans[d] = i-d
                del min_stack[-1]
            min_stack.append(i)  
        return ans

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        n = len(temperatures)
        ans = [0] * n

        if n == 1:
            return [0]

        stk = [(0, temperatures[0])]

        for i in range(1, n):
            temp = temperatures[i]
            if temp <= stk[-1][1]:
                stk.append((i, temp))
            else:
                while stk and stk[-1][1] < temp:
                    j, t = stk.pop()
                    ans[j] = i-j
                stk.append((i, temp))


        return ans

