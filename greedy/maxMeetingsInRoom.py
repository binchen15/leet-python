
# wrong answer. Suspect the solution is wrong

class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here

        meets = list(zip(F, S, range(1, N+1)))
        meets.sort(key = lambda x: (x[0], x[1]))

        ans = [meets[0]]

        i = 1
        while i < N:
            while i < N and meets[i][1] <= ans[-1][0]:
                i += 1
            if i < N:
                ans.append(meets[i])
                i += 1
            else:
                break

        return sorted([meet[2] for meet in ans])

