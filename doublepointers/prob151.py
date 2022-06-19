class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = [word for word in s.split(" ") if word]
        return " ".join(words[::-1])

class Solution:
    def reverseWords(self, s: str) -> str:
        
        n = len(s)
        words = []
        i = 0
        
        while i < n:    
            while i < n and s[i] == " ":
                i += 1
                
            if i < n:
                j = i
                while j + 1 < n and s[j+1] != " ":
                    j += 1
                words.append(s[i:j+1])
                i = j+1

                
        return " ".join(words[::-1])
