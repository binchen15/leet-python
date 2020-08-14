# count good triplets

class Solution(object):

    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        ans = 0
        m = len(arr)
        for i in range(m-2):
            for j in range(i+1, m-1):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, m):
                    if abs(arr[j] - arr[k]) <= b \
                            and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans
