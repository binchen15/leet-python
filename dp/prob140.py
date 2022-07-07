#Word Break II  (50% solution)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        n = len(s)
        ans = []

        if n == 1:
            if s in wordDict:
                return [s]
            else:
                return []

        def walk(arr, i):
            """walk s[i:]"""
            if i == n:
                ans.append(" ".join(arr))
                return
            for word in wordDict:
                if s[i:].startswith(word):
                    walk(arr+[word], i + len(word))

        walk([], 0)

        return ans

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        n = len(s)
        ans = []
        
        if n == 1:
            if s in wordDict:
                return [s]
            else:
                return []
            
        @lru_cache(maxsize=None)    
        def walk(sub, i):
            """walk s[i:]"""
            if i == n:
                ans.append(sub)
                return
            for word in wordDict:
                if s[i:].startswith(word):
                    if not sub:
                        tmp = word
                    else:
                        tmp = sub + " " + word
                    walk(tmp, i + len(word))
                    
        walk("", 0)
        
        return ans
