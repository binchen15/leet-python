class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        offset = ord('a')
        lastIndex = [0] * 26  # the index where each letter occurs for the last time
        for i, c in enumerate(s):
            lastIndex[ord(c)-offset] = i
            
        stack = []
        seen = [False] * 26  # has the letter occured in the stack
        for i, c in enumerate(s):
            if not seen[ord(c)-offset]:
                while stack and stack[-1] > c and lastIndex[ord(stack[-1])-offset] > i:
                    p = stack.pop()
                    seen[ord(p)-offset] = False
                stack.append(c)
                seen[ord(c)-offset] = True
                
        return "".join(stack)
