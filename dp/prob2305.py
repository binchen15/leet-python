# backtrack, timelimit error
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        
        n = len(cookies)
        arr = [0] * k 
        ans = sys.maxsize
        
        def walk(i, arr):
            nonlocal ans
            
            if i == n:
                ans = min(ans, max(arr))
                return
                
            for j in range(k):
                cnt = cookies[i]
                arr[j] += cnt
                walk(i+1, arr)
                arr[j] -= cnt
        
        walk(0, arr)
        
        return ans

# faster, but still timelimit
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        arr = [0] * k
        ans = sys.maxsize

        def walk(i, arr):
            nonlocal ans

            if i == n:
                ans = min(ans, max(arr))
                return

            if max(arr) >= ans:
                return

            for j in range(k):
                cnt = cookies[i]
                arr[j] += cnt
                walk(i+1, arr)
                arr[j] -= cnt

        walk(0, arr)

        return ans

# this passes, but weird
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        n = len(cookies)
        arr = [0] * k
        ans = sys.maxsize

        if n == k:
            return max(cookies)

        def walk(i, arr):
            nonlocal ans

            if i == n:
                ans = min(ans, max(arr))
                return

            if max(arr) >= ans:
                return

            for j in range(k):
                cnt = cookies[i]
                arr[j] += cnt
                walk(i+1, arr)
                arr[j] -= cnt

        walk(0, arr)

        return ans
