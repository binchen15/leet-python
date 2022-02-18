class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        from datetime import datetime, timedelta
        fmt = "%Y-%m-%d"
        d1 = datetime.strptime(date1, fmt)
        d2 = datetime.strptime(date2, fmt)
        
        td = d2 - d1
        return abs(td.days)
