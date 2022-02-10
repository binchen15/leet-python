class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        import math
        
        m = int(math.ceil(n/4))
        r = n % 4
        buf4 = [" "] * 4
        tot = 0
        for i in range(m):
            cnt = read4(buf4)
            if cnt == 0:
                break
            else:
                if i < m-1 or r == 0:
                    # buf.extend(buf4[:cnt])
                    buf[tot:tot+cnt] = buf4[:cnt]
                    tot += cnt
                else:
                    tmp = min(cnt, r)
                    buf[tot:tot+tmp] = buf4[:tmp]
                    tot += tmp
                    
        return tot
